DELIMITER //

CREATE PROCEDURE Q3_CandidatesBySurname(
    IN p_surname VARCHAR(45)
)
BEGIN
    SELECT *
    FROM candidate_details
    WHERE surname = p_surname;
END //

DELIMITER ;