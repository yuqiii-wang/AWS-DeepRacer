# AWS-DeepRacer
The reward function achieved top 10% in competition.

Training Specs:
|---|---|
| Gradient descent batch size	| 64 |
| Entropy	| 0.01 |
| Discount | factor	0.999 |
| Loss type	| Huber |
| Learning rate	| 0.0003 |
| Number of experience episodes between each policy-updating iteration	| 20 |
| Number of epochs	| 10 |

Training Time: 3 Hours

Input Space: 
[0.5, 3.5] m/s 
[-22.5, 22.5] degrees
