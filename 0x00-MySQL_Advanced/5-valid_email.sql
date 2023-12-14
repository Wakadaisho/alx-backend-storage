-- Creates a trigger that resets the attribute valid_email only when the email has been changed

DELIMITER $$
CREATE TRIGGER before_email_changed
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN 
        SET NEW.valid_email = (CASE 
            WHEN NEW.email REGEXP '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}$' THEN 1
            ELSE 0
        END);
    END IF;
END;$$
DELIMITER ;