DELIMITER //

CREATE PROCEDURE Q6_PositionsByRequiredSkill(
    IN p_skill_name VARCHAR(45)
)
BEGIN
    SELECT
        p.position_id,
        p.type_of_position,
        p.hospital_id
    FROM position_details p
    JOIN position_skills ps
        ON p.position_id = ps.position_id
    JOIN skill_details s
        ON ps.skill_id = s.skill_id
    WHERE s.skill_name = p_skill_name;
END //

DELIMITER ;