package StudyCafe.Report;

public class ReportVO {
    private int reportIdx;
    private int reportingUserIdx;
    private String reportingUser;
    private String reportedUser;
    private String reportCategory;
    private String reportDate;
    private String reportStatus;


    public int getReportIdx() {
        return reportIdx;
    }

    public void setReportIdx(int reportIdx) {
        this.reportIdx = reportIdx;
    }

    public String getReportingUser() {
        return reportingUser;
    }

    public void setReportingUser(String reportingUser) {
        this.reportingUser = reportingUser;
    }

    public String getReportCategory() {
        return reportCategory;
    }

    public void setReportCategory(int reportCategory) {
        System.out.println("신고항목 : "+reportCategory);
        if(reportCategory == 1) {
            this.reportCategory = "소음";
        }
        else if(reportCategory == 2) {
            this.reportCategory = "냄새";
        }
        else if(reportCategory == 3){
            this.reportCategory = "음식물 섭취";
        }
    }

    public String getReportDate() {
        return reportDate;
    }

    public void setReportDate(String reportDate) {
        this.reportDate = reportDate;
    }

    public String getReportStatus() {
        return reportStatus;
    }

    public void setReportStatus(int reportStatus) {

        if(reportStatus == 0)   this.reportStatus = "접수완료";
        else if (reportStatus == 1) this.reportStatus = "처리중";
        else    this.reportStatus = "처리완료";
    }

    public int getReportingUserIdx() {
        return reportingUserIdx;
    }

    public void setReportingUserIdx(int reportingUserIdx) {
        this.reportingUserIdx = reportingUserIdx;
    }
}
