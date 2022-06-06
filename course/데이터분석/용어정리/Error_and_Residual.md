> 참고: [Wikipedia](https://en.wikipedia.org/wiki/Errors_and_residuals), [StackOverflow](https://stats.stackexchange.com/questions/133389/what-is-the-difference-between-errors-and-residuals)

# Errors and Residuals

## Wikipedia의 내용을 참고하면,
* The Error:  the deviation of the observed value from the true value of a quantity of interest (for example, a population mean)
* The Residual: the difference between the observed value and the estimated value of the quantity of interest (for example, a sample mean).

## Stakoverflow의 내용을 참고하면, 
* Errors pertain to the true data generating process (DGP), whereas residuals are what is left over after having estimated your model. In truth, assumptions like normality, homoscedasticity, and independence apply to the errors of the DGP, not your model's residuals. (For example, having fit p+1 parameters in your model, only N−(p+1) residuals can be independent.) However, we only have access to the residuals, so that's what we work with.
