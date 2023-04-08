-- A script that creates a stored procedure AddBonus
-- this script adds a new correction for a student.
DELIMITER $$ ;
CREATE PROCEDURE AddBonus(IN id INT, IN projectname varchar(255), IN projectscore INT)
BEGIN
    -- get the project id from the projects table
    SET @project_id = (SELECT id FROM projects WHERE name = projectname);

    -- if the project doesn't exist, insert a new record into the projects table
    IF @project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (projectname);
        SET @project_id = LAST_INSERT_ID(); -- get the id of the newly inserted project
    END IF;

    -- insert or update the score for the specified user and project
    INSERT INTO corrections (user_id, project_id, score) VALUES (id, @project_id, projectscore);
END;
$$
DELIMITER ;
