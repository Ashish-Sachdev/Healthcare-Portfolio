SELECT 
    bc.HEALTH_AUTHORITY,
    bc.PROCEDURE_GROUP,
    bc.COMPLETED_90TH_PERCENTILE * 7 AS bc_90th_days,
    ROUND(bc.COMPLETED_90TH_PERCENTILE, 1) AS bc_90th_weeks
FROM bc_table2 bc
WHERE bc.FISCAL_YEAR = '2024/25'
    AND bc.HEALTH_AUTHORITY NOT IN ('All Health Authorities', 'Provincial Health Services Authority')
    AND bc.HOSPITAL_NAME = 'All Facilities'
    AND bc.PROCEDURE_GROUP IN ('Hip Replacement', 'Knee Replacement', 'Cataract Surgery')
ORDER BY bc_90th_days DESC;