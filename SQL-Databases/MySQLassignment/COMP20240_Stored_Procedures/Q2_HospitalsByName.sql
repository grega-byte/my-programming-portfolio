
DELIMITER //

CREATE PROCEDURE Q2_HospitalsByName(
    IN p_hospital_name VARCHAR(45)
)
BEGIN
    SELECT *
    FROM hospital_details
    WHERE hospital_name = p_hospital_name;
END //

DELIMITER ;