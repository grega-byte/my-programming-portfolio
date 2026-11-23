DELIMITER //

CREATE PROCEDURE Q5_CountCandidatesWithOffers()
BEGIN
    SELECT COUNT(DISTINCT candidate_id) AS total_candidates
    FROM interview_details
    WHERE offer_made = 1;
END //

DELIMITER ;