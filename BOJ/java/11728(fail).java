/*
문제
정렬되어있는 두 배열 A와 B가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 배열 A의 크기 N, 배열 B의 크기 M이 주어진다. (1 ≤ N, M ≤ 1,000,000)

둘째 줄에는 배열 A의 내용이, 셋째 줄에는 배열 B의 내용이 주어진다. 배열에 들어있는 수는 절댓값이 109보다 작거나 같은 정수이다.

출력
첫째 줄에 두 배열을 합친 후 정렬한 결과를 출력한다.
 */
import java.util.*;

public class Main{
	public static void main(String[] args) {
		int N, M;
		int A[];
		int B[];
		StringBuilder Result=new StringBuilder();
		Scanner sc=new Scanner(System.in);
		N=sc.nextInt();
		M=sc.nextInt();
		A=new int[N];
		B=new int[M];
		Arrays.sort(A);
		Arrays.sort(B);
		for(int i=0; i<N; i++) {
			A[i]=sc.nextInt();
		}
		for(int j=0; j<M; j++) {
			B[j]=sc.nextInt();
		}
		int i=0, j=0, k=0;
		while(i<N&&j<M) {
			if(A[i]<B[j]) {
				Result.append(A[i++]+" ");
			}
			else
				Result.append(B[j++]+" ");
		}
		while(i<N) {
			Result.append(A[i++]+" ");
		}
		while(j<M) {
			Result.append(B[j++]+" ");
		}
		System.out.println(Result.toString());
	}
}
