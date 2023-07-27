-- AVG SCORE
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (
	IN user_id INTEGER
)
BEGIN
	DECLARE avg_score FLOAT;
	SET avg_score = (SELECT AVG(score) FROM corrections AS cor WHERE corr.user_id = user_id);
	UPDATE users SET average_score = avg_score WHERE id = user_id;
END
$$
DELIMITER ;
