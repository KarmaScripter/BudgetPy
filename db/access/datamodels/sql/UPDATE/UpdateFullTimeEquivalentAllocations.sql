UPDATE PayrollAccruals
	INNER JOIN ProgramDescriptions
ON ProgramDescriptions.ProgramProjectCode = PayrollAccruals.ProgramProjectCode
SET PayrollAccruals.ProgramAreaCode = ProgramDescriptions.ProgramAreaCode WHERE PayrollAccruals.ProgramProjectCode = ProgramDescriptions.ProgramProjectCode
AND IsNull(PayrollAccruals.ProgramAreaCode);