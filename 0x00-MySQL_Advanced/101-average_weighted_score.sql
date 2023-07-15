-- Create the stored procedure
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE user_id INT;
    DECLARE total_score FLOAT;
    DECLARE total_weight FLOAT;
    
    -- Declare cursor to iterate over users
    DECLARE cur CURSOR FOR SELECT id FROM users;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET @finished = 1;

    -- Open cursor
    OPEN cur;
    SET @finished = 0;
    
    -- Loop through users
    loop_users: LOOP
        -- Fetch user id
        FETCH cur INTO user_id;
        
        -- Exit loop if finished
        IF @finished = 1 THEN
            LEAVE loop_users;
        END IF;

        -- Reset variables
        SET total_score = 0;
        SET total_weight = 0;

        -- Calculate the total weighted score
        SELECT SUM(c.score * p.weight) INTO total_score
        FROM corrections c
        JOIN projects p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the total weight
        SELECT SUM(weight) INTO total_weight
        FROM projects;

        -- Calculate the average weighted score
        UPDATE users
        SET average_score = total_score / total_weight
        WHERE id = user_id;
    END LOOP loop_users;

    -- Close cursor
    CLOSE cur;
END //
DELIMITER ;
