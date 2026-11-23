DELIMITER //

CREATE PROCEDURE Q11_CandidatesInterviewedMoreThanOnce()
BEGIN
    SELECT
        c.candidate_id,
        c.first_name,
        c.surname
    FROM candidate_details c
    JOIN interview_details i
        ON c.candidate_id = i.candidate_id
    GROUP BY
        c.candidate_id,
        c.first_name,
        c.surname
    HAVING COUNT(i.interview_id) > 1;
END //

DELIMITER ;