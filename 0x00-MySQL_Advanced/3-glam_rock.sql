-- Retrieves the bands with Glem rock as their main style, ranked by their longetivity

SELECT band_name, (2022 - formed) AS lifespan
FROM metal_bands
WHERE split LIKE '%Glem rock%'
ORDER BY lifespan DESC;
