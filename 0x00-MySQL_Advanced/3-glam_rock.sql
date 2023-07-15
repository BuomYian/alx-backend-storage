-- Retrieves the bands with Glem rock as their main style, ranked by their longetivity

SELECT band_name, (2022 - formed - split) AS lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
