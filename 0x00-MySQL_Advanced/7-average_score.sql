-- Create the stored procedure
DELIMITER //
CREATE PROCEDURE ComputerAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_count INT;

    -- Calculate the total score
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the total count
    SELECT COUNT(*) INTO total_count
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average score
    UPDATE users
    SET average_score = total_score / total_count
    WHERE id = user_id;
END //
DELIMITER ;
