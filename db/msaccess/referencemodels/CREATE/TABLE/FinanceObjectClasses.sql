﻿PARAMETERS FiscalYearArgs Text ( 255 ), RcCodeArgs Text ( 255 ), FundCodeArgs Text ( 255 );
SELECT PayrollObligations.BFY, PayrollObligations.AhCode AS [AH Code], PayrollObligations.FundCode AS [Fund Code], PayrollObligations.AccountCode AS [Account Code], PayrollObligations.RcCode AS [RC Code], Divisions.Title AS [Division Name], PayrollObligations.PayPeriod AS [Pay Period], PayrollHours.StartDate AS [Start Date], PayrollHours.EndDate AS [End Date], PayrollObligations.FocCode AS [FOC Code], PayrollObligations.FocName AS [FOC Name], PayrollObligations.WorkCode AS [Work Code], PayrollObligations.WorkCodeName AS [Work Code Name], PayrollHours.EmployeeNumber AS [Employee Number], PayrollHours.LastName AS [Last Name], PayrollHours.FirstName AS [First Name], PayrollHours.HumanResourceOrganizationCode AS [HR ORG Code], PayrollHours.HumanResourceOrganizationName AS [HR ORG Name], Sum(PayrollObligations.CumulativeBenefits) AS [Cumulative Benefits], Sum(PayrollObligations.AnnualOvertimePaid) AS [Overtime Paid], Sum(PayrollObligations.AnnualOvertimeHours) AS [Overtime Hours], Sum(PayrollObligations.AnnualBasePaid) AS [Base Paid], Sum(PayrollObligations.AnnualBaseHours) AS [Base Hours], Sum(PayrollObligations.AnnualOtherPaid) AS [Other Paid], Sum(PayrollObligations.AnnualOtherHours) AS [Other Hours], Sum(PayrollObligations.Amount) AS Obligations
FROM Divisions INNER JOIN (PayrollObligations INNER JOIN PayrollHours ON (PayrollObligations.RPIO = PayrollHours.RpioCode) AND (PayrollObligations.PayPeriod = PayrollHours.PayPeriod) AND (PayrollObligations.HumanResourceOrganizationCode = PayrollHours.HumanResourceOrganizationCode) AND (PayrollObligations.WorkCode = PayrollHours.WorkCode)) ON Divisions.Code = PayrollObligations.RcCode
GROUP BY PayrollObligations.BFY, PayrollObligations.AhCode, PayrollObligations.FundCode, PayrollObligations.AccountCode, PayrollObligations.RcCode, Divisions.Title, PayrollObligations.PayPeriod, PayrollHours.StartDate, PayrollHours.EndDate, PayrollObligations.FocCode, PayrollObligations.FocName, PayrollObligations.WorkCode, PayrollObligations.WorkCodeName, PayrollHours.EmployeeNumber, PayrollHours.LastName, PayrollHours.FirstName, PayrollHours.HumanResourceOrganizationCode, PayrollHours.HumanResourceOrganizationName, PayrollHours.ReportingCode, PayrollHours.ReportingCodeDescription
HAVING (((PayrollObligations.BFY)=[FiscalYearArgs]) AND ((PayrollObligations.FundCode)=[FundCodeArgs]) AND ((PayrollObligations.RcCode)=[RcCodeArgs]));
