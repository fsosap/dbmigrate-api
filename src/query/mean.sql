-- List of ids, name and number of employees hired of each department that 
-- hired more employees than the mean of employees hired in 2021 for all the departments

WITH dept_hires AS (
    SELECT
        dept.id,
        COUNT(empl.id)  AS hired
    FROM hired_employees AS empl
    INNER JOIN departments AS dept
        ON empl.department_id = dept.id
    WHERE strftime('%Y', empl.datetime) = '2021'
    GROUP BY dept.id
), mean AS (
    SELECT 
        AVG(hired)  AS _value
    FROM dept_hires
)
SELECT
    dept.id,
    dept.department,
    COUNT(empl.id)  AS hired
FROM hired_employees AS empl
INNER JOIN departments AS dept
    ON empl.department_id = dept.id
INNER JOIN mean
    ON mean._value > 0
GROUP BY dept.id
HAVING COUNT(empl.id) > mean._value
ORDER BY hired DESC