# AWS-DeepRacer
The reward function achieved 42 sec on *re:Invent 2018* by time trial.

Training Specs:

| Hyperparameters | Assignment |
|---|---|
| Gradient descent batch size	| 64 |
| Entropy	| 0.01 |
| Discount factor	| 0.999 |
| Loss type	| Huber |
| Learning rate	| 0.0003 |
| Number of experience episodes between each policy-updating iteration	| 20 |
| Number of epochs	| 10 |

| Training Time |
|---|
| 3 Hours |

| Input Space |
|---|
| [0.5, 3.5] m/s |
| [-22.5, 22.5] degrees |
