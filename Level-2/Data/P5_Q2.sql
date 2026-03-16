SELECT 
    bc.FISCAL_YEAR,
    bc.PROCEDURE_GROUP,
    ROUND(bc.COMPLETED_90TH_PERCENTILE * 7, 1) AS bc_90th_days
FROM bc_table2 bc
WHERE bc.FISCAL_YEAR IN ('2019/20', '2020/21', '2021/22', '2022/23', '2023/24', '2024/25')
    AND bc.HEALTH_AUTHORITY = 'All Health Authorities'
    AND bc.HOSPITAL_NAME = 'All Facilities'
    AND bc.PROCEDURE_GROUP IN ('Hip Replacement', 'Knee Replacement', 'Cataract Surgery')
ORDER BY bc.PROCEDURE_GROUP, bc.FISCAL_YEAR;