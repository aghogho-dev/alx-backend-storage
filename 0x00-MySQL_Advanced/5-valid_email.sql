-- Email validation
DELIMITER ;;
CREATE TRIGGER change_email
BEFORE UPDATE ON users
FOR EACH ROW
	BEGIN
		IF NEW.email != OLD.email
		THEN SET NW.valid_emai = 0;
	END IF;
	END;;
DELIMITER ;
