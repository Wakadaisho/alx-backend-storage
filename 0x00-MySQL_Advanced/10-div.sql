-- Creates a function SafeDiv that divides (and returns) the first by the second number
-- returns 0 for divisions by 0

DELIMITER $$
CREATE FUNCTION SafeDiv (first INT, second INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE result FLOAT DEFAULT 0;

    IF second <> 0 THEN
        SET result = first / second;
    END IF;

    RETURN result;
END;$$
DELIMITER ;