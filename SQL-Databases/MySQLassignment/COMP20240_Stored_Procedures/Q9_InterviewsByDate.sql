DELIMITER //

CREATE PROCEDURE Q9_InterviewsByDate(
    IN p_interview_date DATE
)
BEGIN
    SELECT *
    FROM interview_details
    WHERE interview_date = p_interview_date;
END //

DELIMITER ;