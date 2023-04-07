-- This SQL script select origin column, and sum of fans column as nb_fans, grouped by origin and ordered by nb_fans descending from 'metal_bands' table.

SELECT origin, SUM(fans) AS nb_fans
<<<<<<< HEAD
       FROM metal_bands
       GROUP BY origin
       ORDER BY nb_fans DESC;
=======
    FROM metal_bands
    GROUP BY origin
    ORDER BY nb_fans DESC;
>>>>>>> e54a0a20c6440709a803cfeb73baadca467a2381
