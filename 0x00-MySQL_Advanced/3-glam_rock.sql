-- selects bands who have glam rock as their styles and calculats their lifespans
-- bands with null value as their split values are given 2020 just because for calculation sake

SELECT band_name, (IFNULL(split, 2022) - formed) AS lifespan 
FROM metal_bands 
WHERE FIND_IN_SET('Glam rock', style) > 0 
ORDER BY lifespan DESC;
