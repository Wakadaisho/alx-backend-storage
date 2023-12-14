-- Creates a stored procedure that computes and store the average weighted score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score FLOAT DEFAULT NULL;
    DECLARE w_total FLOAT DEFAULT NULL;

    SELECT SUM(p.weight)
    INTO w_total
    FROM corrections c
    JOIN projects p
    ON c.project_id = p.id
    WHERE c.user_id = user_id;

    SELECT AVG(c.score * (p.weight / w_total))
    INTO avg_score
    FROM corrections c
    JOIN projects p
    ON c.project_id = p.id
    WHERE c.user_id = user_id;

    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END $$
DELIMITER ;
