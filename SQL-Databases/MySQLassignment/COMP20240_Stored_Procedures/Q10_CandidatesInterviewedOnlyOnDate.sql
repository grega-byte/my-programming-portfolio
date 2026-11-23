DELIMITER //

CREATE PROCEDURE Q10_CandidatesInterviewedOnlyOnDate(
    IN p_interview_date DATE
)
BEGIN
    SELECT candidate_id
    FROM interview_details
    GROUP BY candidate_id
    HAVING COUNT(DISTINCT interview_date) = 1
    AND MAX(interview_date) = p_interview_date;
END //

DELIMITER ;