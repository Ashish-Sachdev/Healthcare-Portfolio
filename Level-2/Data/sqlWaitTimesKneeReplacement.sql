SELECT 
    bc.FISCAL_YEAR,
    bc.HEALTH_AUTHORITY,
    bc.COMPLETED_90TH_PERCENTILE * 7 AS bc_90th_days
FROM bc_table2 bc
WHERE bc.PROCEDURE_GROUP = 'Knee Replacement'
    AND bc.HEALTH_AUTHORITY NOT IN ('All Health Authorities', 'Provincial Health Services Authority')
    AND bc.HOSPITAL_NAME = 'All Facilities'
    AND bc.FISCAL_YEAR IS NOT NULL
ORDER BY bc.FISCAL_YEAR, bc.HEALTH_AUTHORITY;