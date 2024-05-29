package StudyCafe.Seats;

public class SeatVO {
    private int seatIdx;  // 좌석 ID
    private int userIdx;  // 사용자 ID
    private String seatStartTime;  // 좌석 사용 시작 시간
    private String seatEndTime;    // 좌석 사용 종료 시간
    private int seatPrice;
    private int waitingUser;

    public SeatVO() {
    }

    public SeatVO(int seatIdx, int userIdx, String seatStartTime, String seatEndTime) {
        this.seatIdx = seatIdx;
        this.userIdx = userIdx;
        this.seatStartTime = seatStartTime;
        this.seatEndTime = seatEndTime;
    }

    public int getSeatIdx() {
        return seatIdx;
    }

    public void setSeatIdx(int seatIdx) {
        this.seatIdx = seatIdx;
    }

    public int getUserIdx() {
        return userIdx;
    }

    public void setUserIdx(int userIdx) {
        this.userIdx = userIdx;
    }

    public String getSeatStartTime() {
        return seatStartTime;
    }

    public void setSeatStartTime(String seatStartTime) {
        this.seatStartTime = seatStartTime;
    }

    public String getSeatEndTime() {
        return seatEndTime;
    }

    public void setSeatEndTime(String seatEndTime) {
        this.seatEndTime = seatEndTime;
    }

    public int getSeatPrice() {
        return seatPrice;
    }

    public void setSeatPrice(int seatPrice) {
        this.seatPrice = seatPrice;
    }

    public int getWaitingUser() {
        return waitingUser;
    }

    public void setWaitingUser(int waiting_user) {
        this.waitingUser = waiting_user;
    }
}