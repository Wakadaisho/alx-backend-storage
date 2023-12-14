-- Creates a stored procedure AddBonus that adds a new correction for a student

DELIMITER $$
CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
	DECLARE project_id INT DEFAULT NULL;

	SELECT `id`
	INTO project_id
	FROM projects p 
	WHERE p.`name` = project_name;

	IF ISNULL(project_id) THEN
		INSERT INTO projects(name) VALUES(project_name);
		SELECT `id`
		INTO project_id
		FROM projects p 
		WHERE p.`name` = project_name;
	END IF;
	
	INSERT INTO corrections
	VALUES (user_id, project_id, score);
END $$
DELIMITER ;
