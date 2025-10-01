![CFAI Logo](https://github.com/wangyongjie-ntu/CFAI/blob/main/CFAI_Logo.png)

<hr/>

[![Maintenance](https://img.shields.io/badge/Maintained%3F-YES-green.svg)](https://github.com/wangyongjie-ntu/Awesome-explainable-AI/graphs/commit-activity)
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)
![](https://img.shields.io/badge/PyTorch%20-%23EE4C2C.svg)

# About CFAI(Counterfactual Explanation for AI on Pytorch)

Counterfactual explanations mainly target to find the mimimum perturbation which changes the original prediction(Ususlly from an undesirable prediction to ideal one). The perturbation itself is a valid instance following the real data distribution as the training samples. It has broad applications, E.g., finance, education, health care ect. Specifically, what should I do to get the credit card approved if I received the rejection.

This task is popular recently. However, I only find few released repositories on Pytorch platform. Hence, I create this project and plan to implement some famous algorithms continously. 
I appreciate it very much if anyone can contribute to this project together with me.  For the implementation details, I am glad to discuss with all of you together.

A collection of methods on counterfactual explanation to add into this repository. Continously updating.

- [x] PlainCF, [Counterfactual explanations without opening the black box: Automated decisions and the GDPR](https://arxiv.org/pdf/1711.00399.pdf) [1]

- [x] DiCE, [Explaining machine learning classifiers through diverse counterfactual explanations](https://arxiv.org/pdf/1905.07697.pdf)[2]

- [x] Growing Sphere, [Inverse Classification for Comparison-based Interpretability in Machine Learning](https://arxiv.org/abs/1712.08443)[3]

- [ ] REVISE, [Towards Realistic Individual Recourse and Actionable Explanations in Black-Box Decision Making Systems](https://arxiv.org/pdf/1907.09615.pdf)[4]

- [ ] CEM, [Explanations based on the Missing: Towards contrastive explanations with pertinent negatives](https://papers.nips.cc/paper/2018/file/c5ff2543b53f4cc0ad3819a36752467b-Paper.pdf)[5]

# Installation

This is a half-year plan. The installation just serves as a placeholder.

**Installation Requirements**
- Pytorch >= 1.0+
- Python >= 3.6

CF only supports Python3+. If you want to install the latest version, run the command in the root folder
```
git clone https://github.com/wangyongjie-ntu/CFAI

cd CFAI

pip install -e .
```

For the stable version installation, you can directly install it from PyPI via

```
pip install cfai
```


# Getting Start

To be done.

# References

[1] Wachter, Sandra, Brent Mittelstadt, and Chris Russell. "Counterfactual explanations without opening the black box: Automated decisions and the GDPR." Harv. JL & Tech. 31 (2017): 841. [https://arxiv.org/pdf/1711.00399.pdf](https://arxiv.org/pdf/1711.00399.pdf)

[2] Mothilal, Ramaravind K., Amit Sharma, and Chenhao Tan. "Explaining machine learning classifiers through diverse counterfactual explanations." Proceedings of the 2020 Conference on Fairness, Accountability, and Transparency. 2020.
[https://arxiv.org/pdf/1905.07697.pdf](https://arxiv.org/pdf/1905.07697.pdf)

[3] Laugel, Thibault, et al. "Inverse classification for comparison-based interpretability in machine learning." arXiv preprint arXiv:1712.08443 (2017).[https://arxiv.org/abs/1712.08443](https://arxiv.org/abs/1712.08443)

[4] Joshi, Shalmali, et al. "Towards realistic individual recourse and actionable explanations in black-box decision making systems." arXiv preprint arXiv:1907.09615 (2019). [https://arxiv.org/pdf/1907.09615.pdf](https://arxiv.org/pdf/1907.09615.pdf)

[5] Dhurandhar, Amit, et al. "Explanations based on the missing: Towards contrastive explanations with pertinent negatives." Advances in neural information processing systems 31 (2018): 592-603. [https://papers.nips.cc/paper/2018/file/c5ff2543b53f4cc0ad3819a36752467b-Paper.pdf](https://papers.nips.cc/paper/2018/file/c5ff2543b53f4cc0ad3819a36752467b-Paper.pdf)

# Acknowledge

If any questions on this repo, please kindly let me know by email(yongjie.wang@ntu.edu.sg)

