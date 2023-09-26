import java.util.List;
public class RegionReport {
    List<Integer> temp;
    String currentRating;
    String windDirection;

    int windSpeedH;
    int windSpeedL;

    public RegionReport(){}

    public String getCurrentRating() {
        return currentRating;
    }

    public int getWindSpeedH() {
        return windSpeedH;
    }

    public int getWindSpeedL() {
        return windSpeedL;
    }

    public String getWindDirection() {
        return windDirection;
    }

    public int getTemp(int index) {
        return temp.get(index);
    }
    public List<Integer> getTempList(){
        return temp;
    }

    public void addTemp(int newTemp){
        temp.add(0,newTemp);
    }

    public void setCurrentRating(String currentRating) {
        this.currentRating = currentRating;
    }

    public void setTemp(List<Integer> temp) {
        this.temp = temp;
    }

    public void setWindSpeedH(int windSpeedH) {
        this.windSpeedH = windSpeedH;
    }

    public void setWindSpeedL(int windSpeedL) {
        this.windSpeedL = windSpeedL;
    }

    public void setWindDirection(String windDirection) {
        this.windDirection = windDirection;
    }


}
