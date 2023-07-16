-- Procedure to add a new correction for a student
DELIMITER //

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    -- Variable to hold the project ID
    DECLARE project_id INT;

    -- Check if the project already exists
    SELECT id INTO project_id FROM projects WHERE name = project_name;

    -- If the project doesn't exist, create it
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Insert the correction
    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);

    -- Update the average score for the user
    UPDATE users SET average_score = (
        SELECT AVG(score) FROM corrections WHERE user_id = user_id
    ) WHERE id = user_id;

END //

DELIMITER ;