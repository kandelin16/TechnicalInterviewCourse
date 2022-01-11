function fibbonacci(n) {
    if (n==1 || n==0) {
        return n
    }
    else {
        return fibbonacci(n-1) + fibbonacci(n-2)
    }
}