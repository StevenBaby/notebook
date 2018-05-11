# Linux 通过网络同步系统时间

## NTP 服务

NTP 是网络时间协议(Network Time Protocol), 它用来同步网络中各个计算机的时间。

在计算机的世界里，时间非常地重要，例如对于火箭发射这种科研活动，对时间的统一性和准确性要求就非常地高，是按照A这台计算机的时间，还是按照B这台计算机的时间？NTP就是用来解决这个问题的，NTP（Network Time Protocol，网络时间协议）是用来使网络中的各个计算机时间同步的一种协议。它的用途是把计算机的时钟同步到世界协调时UTC，其精度在局域网内可达0.1ms，在互联网上绝大多数的地方其精度可以达到1-50ms。

它可以使计算机对其服务器或时钟源（如石英钟，GPS等等）进行时间同步，它可以提供高精准度的时间校正，而且可以使用加密确认的方式来防止病毒的协议攻击。

### 原理

NTP要提供准确的时间，就必须有准确的时间来源，那可以用格林尼治时间吗？答案是否定的。因为格林尼治时间是以地球自转为基础的时间计量系统，但是地球每天的自转是有些不规则的，而且正在缓慢加速，因此，格林尼治时间已经不再被作为标准时间使用。

新的标准时间，是由原子钟报时的国际标准时间UTC（Universal Time Coordinated，世界协调时）。所以NTP获得UTC的时间来源可以是原子钟、天文台、卫星，也可以从Internet上获取。

有了准确而可靠的的时间源，那这个时间如何传播呢？在NTP中，定义了时间按照服务器的等级传播，按照离外部UTC源远近将所有的服务器归入不同的Stratum（层）中，例如把通过GPS（Global Positioning System，全球定位系统）取得发送标准时间的服务器叫Stratum-1的NTP服务器，而Stratum-2则从Stratum-1获取时间，Stratum-3从Stratum-2获取时间，以此类推，但Stratum层的总数限制在15以内。所有这些服务器在逻辑上形成阶梯式的架构相互连接，而Stratum-1的时间服务器是整个系统的基础，这种阶梯式的架构示意图如图所示。

![NTP阶梯式的架构示意图](https://gss2.bdstatic.com/9fo3dSag_xI4khGkpoWK1HF6hhy/baike/s%3D220/sign=62efb143a4efce1bee2bcfc89f51f3e8/d0c8a786c9177f3e95090eb873cf3bc79f3d5642.jpg)


计算机主机一般同多个时钟服务器连接，利用统计学的算法过滤来自不同服务器的时间，以选择最佳的路径和来源以便校正主机时间。即使在主机长时间无法与某一时钟服务器联系的情况下，NTP服务依然可以有效运转。
为了防止对时钟服务器的恶意破坏，NTP使用了识别机制，检查发送来的信息是否是真正来自所宣称的时钟服务器并检查信息的返回路径，以提供对抗干扰的保护机制。

NTP时间同步报文中包含的时间是格林威治时间，是从1900年开始计算的秒数。

### 发展

NTP首次记载是在Internet Engineering Note之中，其精确度为百毫秒。稍后出现了首个时间协议的规范，即RFC-778，它被命名为DCNET互联网时间服务，而它提供这种服务还是借助于ICMP（Internet Control Message Protocol，Internet控制报文协议），即互联网控制消息协议中的时间戳消息和时间戳应答消息作为NTP。

NTP名称的首次出现是在RFC-958之中，该版本也被称为NTP Version0，其目的是为ARPA（Advanced Research Projects Agency，美国国防部高级研究计划署）的网络提供时间同步。它已完全脱离ICMP，是作为独立的协议以便完成更高要求的时间同步功能。它对于本地时钟的误差估算和精密度等基本运算、参考时钟的特性、网络上的分组数据包及其消息格式者进行了描述。但是不对任何频率误差进行补偿，也没有规定滤波和同步的算法。

美国特拉华大学（University of Delaware）的David L .Mills主持了由DARPA（Defense Advanced Research Projects Agency，美国国防部高级研究计划局）、NSF（National Science Foundation，美国国家科学基金）和NSWC（Naval Surface Warfare Center，美国海军水面武器中心）资助的网络时间同步项目，成功的开发出了NTP协议的Version1、Version2和Version3 三个版本。

NTP Version1出现于1988年6月，在RFC-1059中描述了首个完整的NTP规范和相关算法。这个版本已经采用了客户端/服务器端（Client/Server）模式以及对称操作，但是它不支持授权鉴别和NTP的控制消息。

1989年9月推出了取代RFC-958和RFC-1059的NTP Version2版本即RFC-1119。

几乎同时，DEC公司也推出了一个时间同步协议DTSS（Digital Time Synchronization Service，数字时间同步服务）。在1992年3月，NTP Version3版本RFC-1305问世，该版本总结和综合了NTP之前的所有版本和DTSS，正式引入了校正原则，并改进了时钟选择和时钟滤波的算法，而且还引入了时间消息发送的广播模式，这个版本取代了NTP的先前版本。

NTP Version3发布后，一直在不断地进行改进，NTP实现的一个重要功能是对计算机操作系统的时钟调整。在NTP Version3研究和推出的同时，有关在操作系统核心中改进时间保持功能的研究也在并行地进行。

1994年推出了RFC-1589，名为A KernelModel for Precision Time keening，即精密时01保持的核心模式，这个实现可以把计算机操作系统的时间精确度保持在微秒数量级。

截止到2010年6月，最新的NTP版本是第4版（NTP Version 4），其标准化文档为RFC 5905，它继承自RFC 1305所描述的NTP Version3。网络时间同步技术也将向更高精度、更强的兼容性和多平台的适应性方向发展。


## ntp服务器

- cn.pool.ntp.org 中国ntp服务器

## 具体操作

安装 ntp:

    pacman -S ntp

执行命令:

    ntpdate cn.pool.ntp.org


## 参考资料

- [1] ntp_百度百科 <https://baike.baidu.com/item/NTP/1100433>