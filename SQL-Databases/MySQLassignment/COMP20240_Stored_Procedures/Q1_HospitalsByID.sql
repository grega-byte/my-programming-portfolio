DROP PROCEDURE IF EXISTS q1_hospitals_by_id;

DELIMITER //

CREATE PROCEDURE Q1_HospitalsByID(
    IN p_hospital_id INT
)
BEGIN
    SELECT *
    FROM hospital_details
    WHERE hospital_id = p_hospital_id;
END //

DELIMITER ;