DELIMITER //

CREATE PROCEDURE Q4_CandidatesByPositionID(
    IN p_position_id INT
)
BEGIN
    SELECT DISTINCT
        c.candidate_id,
        c.first_name,
        c.surname
    FROM candidate_details c
    JOIN candidate_skills cs
        ON c.candidate_id = cs.candidate_id
    JOIN position_skills ps
        ON cs.skills_id = ps.skill_id
    WHERE ps.position_id = p_position_id;
END //

DELIMITER ;