-- Old school
SELECT
	band_name,
	IFNULL(split, 2020) - IFNULL(formed, 0) lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%';
