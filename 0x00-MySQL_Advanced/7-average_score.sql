-- Stored procedure that computes and stores the average score for a student

DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE average_score FLOAT DEFAULT NULL;

    SELECT AVG(c.score)
    INTO average_score
    FROM corrections c
    WHERE c.user_id = user_id;

    UPDATE users
    SET average_score = average_score
    WHERE id = user_id;
END $$
DELIMITER ;