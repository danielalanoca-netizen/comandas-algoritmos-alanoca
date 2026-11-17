Alanoca Alfaro Daniel Antony
a) Complejidad de cada fragmento
- F1 — O(n): recorre los n elementos una vez y hace trabajo constante en cada iteración.
- F2 — O(n²): compara cada elemento con los que le siguen; suma \(n(n-1)/2\) comparaciones.
- F3 — O(log n): k empieza en n y se divide entre 2 hasta llegar a 1.
- F4 — O(n log n): el bucle exterior se repite n veces; en cada vuelta, k se duplica hasta n, lo que tarda O(log n).
b) Recurrencias
(i) \(T(n)=3T(n/2)+n\)

\(a=3,\ b=2,\ d=1\). Como \(a=3>b^d=2^1=2\), resulta:
\[
T(n)=\Theta(n^{\log_2 3})
\]
(ii) \(T(n)=T(n/2)+n^2\)

\(a=1,\ b=2,\ d=2\). Como \(a=1<b^d=2^2=4\), resulta:
\[
T(n)=\Theta(n^2)
\]