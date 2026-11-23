DELIMITER //

CREATE PROCEDURE Q7_CountNursingPositions()
BEGIN
    SELECT COUNT(DISTINCT ps.position_id) AS total_positions
    FROM position_skills ps
    JOIN skill_details s
        ON ps.skill_id = s.skill_id
    WHERE s.skill_name = 'Nursing';
END //

DELIMITER ;