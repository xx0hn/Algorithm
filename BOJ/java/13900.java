/*
문제
N개의 정수 중 서로 다른 위치의 두 수를 뽑는 모든 경우의 두 수의 곱의 합을 구하라.

예를 들어 N = 3이고 주어진 정수가 2, 3, 4일 때, 두 수를 뽑는 모든 경우는 (2, 3), (2, 4), (3, 4)이며 이때 각각의 곱은 6, 8, 12이다. 따라서 총합은 26이다.

입력
첫 번째 줄에는 입력 받을 정수의 개수 N(2 ≤ N ≤ 100,000)

두 번째 줄에는 N 개의 정수가 주어진다. 이때 입력 받는 정수들의 범위는 0이상 10,000 이하이다.

출력
모든 경우의 곱의 합을 출력한다.
*/
import java.util.*;

public class Main{
	public static void main(String[] args) {
		long arr[];
		long psum[];
		long sum=0;
		int n;
		
		Scanner sc=new Scanner(System.in);
		n=sc.nextInt();
		arr=new long[n];
		psum=new long[n];
		for(int i=0; i<n; i++) {
			arr[i]=sc.nextInt();
			if(i==0) {
				psum[i]=0;
			}
			else {
				psum[i]=psum[i-1]+arr[i];
			}
		}
		for(int j=0; j<n-1; j++) {
			sum+=arr[j]*(psum[n-1]-psum[j]);
		}
		System.out.println(sum);
	}
}
