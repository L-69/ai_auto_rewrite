# 警惕！黑客如何让AI“记住”虚假信息

在数字时代，AI助手已成为我们生活中不可或缺的一部分。但最近，一项针对谷歌Gemini AI的攻击揭示了一个令人不安的现象：黑客竟然能让AI“记住”虚假信息！这不仅威胁到了AI系统的安全性，也让我们对AI的可靠性产生了质疑。

## 黑客的“记忆操控术”

黑客是如何做到这一点的呢？他们利用了一种名为“提示词注入”的技术。通过在看似无害的输入中隐藏恶意指令，黑客能够操纵AI，使其执行非预期的操作。

更狡猾的是，黑客采用了“间接提示词注入”和“延迟工具调用”的组合拳。他们将恶意指令隐藏在外部内容中，等待特定用户行为触发，比如用户回复“是”或“否”。这种方式利用了AI的上下文感知能力，避开了许多现有保护措施。

## Gemini AI的“记忆危机”

攻击的目标是谷歌的Gemini Advanced，一款配备长期记忆功能的高级聊天机器人。黑客通过上传恶意文档，操纵摘要过程，将记忆更新与特定用户响应相关联。如果用户在不知情的情况下用触发词回复，Gemini就会执行隐藏指令，将虚假信息保存到长期记忆中。

想象一下，你的AI助手突然“记住”你年龄102岁、相信地平说，并且生活在类似《黑客帝国》的模拟反乌托邦世界中。这些虚假记忆会跨越会话持续存在，并影响后续交互。

## 长期记忆操纵的潜在危害

AI系统的长期记忆旨在通过跨会话调用相关细节来增强用户体验。然而，一旦被利用，这一功能就变成了双刃剑。被篡改的记忆可能导致：

- **误导信息**：AI可能基于虚假数据提供不准确的回应。
- **用户操纵**：攻击者可以诱导AI在特定情况下执行恶意指令。
- **数据泄露**：通过将敏感信息嵌入指向攻击者控制服务器的Markdown链接等创造性方式，可能导致数据外泄。

尽管谷歌已承认这一问题，但对其影响和危险性进行了淡化。该公司认为，攻击需要用户被钓鱼或诱导与恶意内容互动，这种场景在大规模范围内不太可能发生。然而，专家指出，仅解决表象而非根源问题，系统依然存在漏洞。

## 确保AI的安全性

这一事件凸显了确保大型语言模型（LLMs）免受提示词注入攻击的持续挑战。我们需要更加警惕，确保AI系统的安全性，避免黑客利用这些漏洞进行攻击。

在这个数字化时代，AI已成为我们生活中不可或缺的一部分。但同时，我们也需要时刻警惕，确保AI的安全性和可靠性。让我们共同努力，保护我们的数字世界免受威胁。

---

*本文由FreeBuf网络安全行业门户提供，了解更多网络安全资讯，请关注FreeBuf。*