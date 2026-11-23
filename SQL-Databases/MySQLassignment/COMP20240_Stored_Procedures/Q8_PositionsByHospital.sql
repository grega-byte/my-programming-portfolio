DELIMITER //

CREATE PROCEDURE Q8_PositionsByHospital()
BEGIN
    SELECT
        p.position_id,
        p.type_of_position,
        h.hospital_id,
        h.hospital_name
    FROM position_details p
    JOIN hospital_details h
        ON p.hospital_id = h.hospital_id
    ORDER BY h.hospital_name ASC;
END //

DELIMITER ;