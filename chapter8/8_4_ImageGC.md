---
marp: true
theme: MyGaia
paginate: true
---

<!-- _class: lead -->
## 图像和音频生成

---

### **GPU和CUDA**

+ **GPU（Graphic Process Unit，图形处理单元）**：是一种专门为处理图形数据和执行并行计算而设计的处理器。它具有大量的核心和高速的内存带宽，能够同时处理多个计算任务，特别适合处理具有高度并行性的数据，如在图像和视频处理、深度学习等领域。

+ **CUDA（Compute Unified Device Architecture，统一计算设备架构）**：是英伟达公司推出的一种并行计算平台和编程模型，包含了CUDA指令集架构以及GPU内部的并行计算引擎。开发人员可以使用C、C++等语言来为CUDA架构编写程序，让程序在支持CUDA的英伟达GPU上以超高性能运行，大大提高计算效率。

---

### **GPU和CUDA**

+ 大模型生成图片涉及大量矩阵运算和数据处理，GPU的并行计算能力可同时处理众多任务，大幅缩短生成时间。同时，生成高分辨率图像需大量计算资源，GPU能提供足够计算能力和显存，保证图像细节与质量。其并行处理能力可在合理时间内完成复杂视觉效果和风格迁移计算，提供丰富创作选项。

+ CUDA为开发人员提供了一种便捷的方式来利用GPU的强大计算能力。通过CUDA，开发人员可以将大模型中的计算任务并行化，将其分配到GPU的多个核心上同时执行，从而大大提高模型的训练和推理速度，进而加速图片的生成过程。以下是系统安装CUDA和cuDNN的方法（以Windows系统为例）：

---

### **GPU和CUDA**

**安装前准备：**

- 确认硬件支持：确保计算机配备NVIDIA GPU，且该GPU支持CUDA。在Windows系统中，打开命令提示符（CMD），输入`"nvidia -smi"`命令可查看GPU型号及驱动版本。

- 选择合适的版本：CUDA和cuDNN的版本需相互兼容，且与操作系统、GPU型号以及使用的深度学习框架相匹配。可通过NVIDIA官方网站查询支持的CUDA版本，再根据深度学习框架选择合适的版本。

---

### **GPU和CUDA**

**安装CUDA和cuDNN**

- 下载CUDA安装包：访问NVIDIA官方网站的CUDA Toolkit下载页面，选择适合操作系统和GPU型号的CUDA版本，通常是exe文件。
- 安装CUDA：双击安装包，按提示进行安装。
- 验证CUDA安装：打开命令提示符（CMD），输入"nvcc -V"，若返回版本信息，说明CUDA安装正确。

- 访问NVIDIA cuDNN下载页面，下载cuDNN的安装程序，运行安装即可。

---

### **潜空间表示**

本节我们来讨论图像、视频或文本任务的高效数据表示。为什么高效的表示很重要呢？我们希望在保留数据本质特征的同时，减少需要存储和处理的信息量。丰富的表示能够训练针对特定任务的模型，并且使表示形式紧凑可以降低训练和使用数据密集型模型时的计算要求。例如，对图像的向量嵌入进行训练，相比直接对图像的像素进行训练，效率更高且表现力更强。

像ZIP或JPEG这样的传统压缩方法专注于特定的数据类型，并使用手工设计的算法来减小文件大小。虽然这些方法在其预定用途上很有效，但它们缺乏所学压缩技术的灵活性和适应性。例如，ZIP通过识别和编码重复模式，在无损压缩通用数据方面表现出色。另一方面，JPEG专门为图像压缩而设计，通过丢弃不太明显的视觉信息来显著减小文件大小。然而，这些传统方法不会从它们所压缩的数据中学习，并且除了减小大小之外，无法自动适应不同类型的内容，也不能针对特定任务进行优化。而这些缺点，可以通过机器学习模型来解决。

自动编码器是一类机器学习模型，由一个"压缩"数据的编码器和一个重建数据的解码器组成。编码器学习它需要关注的数据的基本特征，解码器能够逆转这些变换。这种训练方法是一种无需依赖手工设计算法就能自动构建压缩器的方式。压缩信息（即使是以有损的方式）本身就很有用，但一旦拥有了紧凑的数据集表示，还能做一些其他有趣的事情。

如果系统经过正确训练，并且解码器能够从压缩表示中恢复原始数据，这意味着所学的表示已经捕获了基本信息。因此，对表示进行操作等同于对原始数据进行操作，但所需的内存和计算量要少得多。这是像稳定扩散（Stable
Diffusion）这类模型的关键设计方面之一。在后续章节，我们可以生成和处理大图像，但大部分计算发生在表示所在的较小的潜在空间中。

因为所学的表示捕获了基本信息，所以在自动编码器训练完成后，可以拆分编码器和解码器，并将编码器用作特征提取组件。在编码器的输出之上添加一个小型网络，能够针对不同的任务（如文本或图像分类）来训练模型。这些小型网络不是对整个输入图像进行操作，而是对编码器获得的基本特征进行操作。

还可以将不同的数据类型编码为相同的潜在空间表示。序列到序列的语言模型使用编码器-解码器架构来执行各种各样的任务，比如翻译或总结。尽管在设计这样的系统时需要考虑更多细节，但一个关键的要点是，编码器的任务是捕捉那些承载着关于输入文本足够语义信息的基本特征。这也适用于跨模态的情况：例如，图像字幕模型的任务是利用潜在空间作为内部工作数据，将图像表示转换为文本描述。

自动编码器的另一个应用示例是生成式建模。在训练好编码器-解码器对之后，可以舍弃编码器，并通过从潜在空间的随机分布中采样来生成新的数据。这就是变分自动编码器（VAE）的基础。

下面将使用图像数据来展示自动编码器和变分自动编码器的工作原理，但这些技术不仅限于图像，还可以应用于任何数据。本章的最后一部分将研究多模态表示学习系统（如CLIP）如何弥合文本和图像之间的差距，并可用于非常有趣的应用场景，比如语义搜索、数据过滤、文本到图像的生成等等。

自动编码器（AutoEncoder）是一种无监督学习的神经网络模型，主要由编码器和解码器两部分组成，其工作原理如下：

**编码过程：**
编码器的作用是将输入数据压缩成一个低维的表示，这个过程也被称为特征提取。它会学习输入数据的内在结构和特征，将原始数据映射到一个潜在空间中。例如，对于一幅图像，编码器会自动识别图像中的边缘、颜色、纹理等基本特征，并将这些特征用一个低维向量来表示。在这个过程中，编码器通过一系列的线性或非线性变换，将高维的输入数据逐步压缩成低维的编码向量。

**解码过程：**解码器的任务是根据编码器生成的低维编码向量，尝试重建出原始的输入数据。它是编码器的逆过程，通过学习将低维编码向量映射回原始数据空间。例如，对于前面编码后的图像向量，解码器会根据这个向量尝试恢复出原始的图像。它会通过一系列的反变换，将低维向量逐步扩展成与原始输入数据相同维度的输出。

**训练过程：**自动编码器的训练目标是最小化重建误差，即让解码器输出的结果尽可能接近原始输入数据。在训练过程中，通过不断调整编码器和解码器的参数，使得重建误差逐渐减小。例如，使用均方误差（MSE）作为损失函数，计算原始输入与重建输出之间的差异，并通过反向传播算法来更新神经网络的权重，使得损失函数的值不断降低。通过大量的数据训练，自动编码器能够学习到数据的有效表示，使得编码器提取的特征能够包含足够的信息，让解码器准确地重建出原始数据。通过这种方式，自动编码器能够学习到数据的高效表示，在保留数据本质特征的同时实现数据的压缩和重建，并且可以将编码器作为特征提取器用于其他任务，如分类、聚类等。下面来看一个具体的例子。

**1. 需要导入的包：**

    import torch
    import torch.nn as nn
    import torch.nn.functional as F
    import torch.optim as optim
    import PIL.Image as Image
    import numpy as np

    from torchvision.transforms import ToTensor, Resize, Compose
    from torch.utils.data import DataLoader, Dataset
    from pathlib import Path
    from matplotlib import pyplot as plt

**2. 数据准备：**

这个例子使用了一个动漫头像的图片集。该数据及可以从kaggle网站下载（有许多网站都提供下载，但图片数量不同）https://www.kaggle.com/datasets/splcher/animefacedataset。从kaggle下载的数据集包含了63535张动漫图像jpg格式的图片。大部分的图片大小是64\*64像素的，少量不同。下载后解压缩，得到一个文件夹，该文件里包含了所有的图片。

虽然pytorch提供了一个处理图片的类，但那个类主要是针对图片分类的，我们从dataset继承一个自己的类，来处理这些图片并转换成pytorch的dataset。

    class ImageFile(Dataset):
    def __init__(self, image_path, transform=None):
    	  # 图片路径
            self.image_path = Path(image_path)
            self.transform = transform
    	  # 获取所有图片文件
            image_extensions = ('*.jpg', '*.jpeg', '*.png', '*.gif')
            self.image_files = [file for ext in image_extensions 
                                for file in self.image_path.glob(ext)]
        
        def __len__(self):
            return len(self.image_files)

        def __getitem__(self, idx):
            image_file = self.image_files[idx]
            image = Image.open(image_file).convert('RGB')
            if self.transform:
                image = self.transform(image)
            return image, image

从dataset类继承的类至少要实现2个方法。1个是方法\_\_len\_\_，该方法返回整个给数据集的大小。一个是\_\_getitem\_\_该方法根据给出的索引，返回数据集的一项。注意最后的return，将同样的图片返回了2次。第一个图片对应的是x值，该图片经过编码后再经过解码还原，和第2个图片y比较差异。当然也可以只返回一个图片，那样需要在编码前保存好原始的图片。我们将所有图片统一变换成64\*64，然后转为pytorch的张量，这通过下面的transform来完成：

    transform = Compose([
        Resize((64,64)),
        ToTensor(),
    ])
    image_path = './data/images'

注意需要把上面代码中的图片路径替换为你自己的路径，也就是图片文件夹的存储位置。随后就可以创建dataset和dataloader了。这些过程和第七章的是一样的。

    ImageDataset = ImageFile(image_path=image_path, transform=transform)
    train_loader = DataLoader(ImageDataset, batch_size=128, shuffle=True)

到此，准备好了数据，显示数据库的前10幅图像看一下：

    fig, ax = plt.subplots(1, 10)
    for i in range(10):
        train = ImageDataset[i][0].permute(1, 2, 0).numpy()
        ax[i].imshow(train)
        ax[i].axis('off')

![](images8/media/image3.png){width="5.364583333333333in"
height="0.6458333333333334in"}

**3. 编码器：**

首先将为自动编码器的编码器部分创建一个模型定义。由于处理的是图像数据，一个自然的选择是使用卷积层，它擅长捕捉图像特征。针对这个问题，还可以考虑许多其他方案：全连接层、Transformer模块、使用残差跳跃连接等等。

我们将使用一个简单的卷积编码器，编码器将堆叠几个卷积层，每层将添加一个批量归一化层（BatchNorm2d）和一个激活函数（在这个例子中，使用ReLU激活函数）。在训练过程中，批量归一化会使用当前批次数据的均值和标准差来对输入数据进行归一化，以便使其保持在可预测的范围内，这在大多数情况下会使训练过程更加平稳且快速。如前所述，编码器的实现将是一系列的卷积层。每一层会逐步降低图像分辨率，同时将表示的通道数增加到1024。最后，在末尾添加一个全连接层，以创建256维的向量表示。代码中的注释展示了输入数据在经过各层时其形状是如何变换的：

    class Encoder(nn.Module):
        def __init__(self, in_channels=3):
            super().__init__()
            self.con_block = nn.Sequential(
                # 3@64x64 -> 64@32x32
                nn.Conv2d(in_channels, 64, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(64),
                # 64@32x32 -> 128@16x16
                nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(128),
                # 128@16x16 -> 256@8x8
                nn.Conv2d(128, 256, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(256),
                # 256@8x8 -> 512@4x4
                nn.Conv2d(256, 512, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(512),
                # 512@4x4 -> 1024@1x1
                nn.Conv2d(512, 1024, kernel_size=4, stride=2, padding=0),
                nn.ReLU(),
                nn.BatchNorm2d(1024),
            )
            self.fc_block = nn.Sequential(
                nn.Linear(1024, 512),
                nn.ReLU(),
                nn.Linear(512, 256),
            )
        
        def forward(self, x):
            x = self.con_block(x)
            # shape: (batch_size, 1024, 1, 1)
            x = x.flatten(start_dim=1)
            # shape: (batch_size, 1024)
            x = self.fc_block(x)
            # shape: (batch_size, 256)
            return x       

输入的3通道64\*64的图片经过卷积层逐步变换为1\*1，但同时通道数有3增加到了1024。最后通过一个全连接层将1024维降到了256。也就是说，一个3\*64\*64的图像最后用一个256维的向量来表示。数据量从12288（3\*64\*64的值）降到了256。

Shape的变化：前面的代码中指定的batch的大小是128，pytorch框架处理图片约定使用NCWH的格式，也就是第一维是batch的大小，第二维是图片的通道数，接下来是图片的宽度和高度。对于本例，Encode的输入张量的shape是（128，3，64，64）输出是（128，256）。

**4. 解码器：**

解码器从编码器得到的潜在表示（256维向量）开始，将它们转换为原始尺寸的图像。解码器的架构不一定非得是编码器架构的逆形式；它可以是任何能够"理解"编码器表示，并能够将这些表示转换为图像的架构。在这个例子中，将创建一个与编码器大致对称的网络：应用转置卷积来提高分辨率，同时减少通道数量，直到达到期望的3\*64\*64像素的输出分辨率。

在转置卷积之前添加一个全连接层，以创建具有1024\*1\*1像素的张量。这一层将被重塑为1\*1分辨率（\[1024,
1,
1\]）也就是具有1024个通道的1\*1的图像作为第一个转置卷积的输入。从这里开始，逐步减少通道数量并提高分辨率，直到达到原始图像的形状。还有其他方法可以达到相同的效果；请记住，输入是一个具有256个通道的扁平向量，而输出必须是3个通道且为64\*64像素的图像。

    class Decoder(nn.Module):
        def __init__(self, out_channels=3):
            super().__init__()
            self.fc_block = nn.Sequential(
                # shape: (batch_size, 256) -> (batch_size, 2048)
                nn.Linear(256, 512),
                nn.ReLU(),
                # shape: (batch_size, 512) -> (batch_size, 1024)
                nn.Linear(512, 1024),
                nn.ReLU(),
            )
            self.con_block = nn.Sequential(
                # 1024@1x1 -> 512@4x4
                nn.ConvTranspose2d(1024, 512, kernel_size=4, stride=1, padding=0),
                nn.ReLU(),
                nn.BatchNorm2d(512),
                # 512@4x4 -> 256@8x8
                nn.ConvTranspose2d(512, 256, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(256),
                # 256@8x8 -> 128@16x16
                nn.ConvTranspose2d(256, 128, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(128),
                # 128@16x16 -> 64@32x32
                nn.ConvTranspose2d(128, 64, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(64),
                # 64@32x32 -> 3@64x64
                nn.ConvTranspose2d(64, out_channels, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(out_channels),
            )
        
        def forward(self, x):
            x = self.fc_block(x)
            # shape: (batch_size, 1024)
            x = x.view(-1, 1024, 1, 1)
            # shape: (batch_size, 1024, 1, 1)
            x = self.con_block(x)
            # shape: (batch_size, out_channels, 64, 64)
            return (F.tanh(x)+1)/2

对最后的输出应用的双曲正切函数，将输出的数值限制在了\[0,1\]之间。通过解码器，从256维的向量还原了图像。将编码器和解码器组合起来，就得到了AutoEncoder：

    class AutoEncoder(nn.Module):
        def __init__(self, in_channels=3, out_channels=3):
            super().__init__()
            self.encoder = Encoder(in_channels=in_channels)
            self.decoder = Decoder(out_channels=out_channels)
        
        def forward(self, x):
            x = self.encoder(x)
            x = self.decoder(x)
            return x

**5. 训练**

到目前为止，已经创建了编码器和解码器。编码器用于降低输入图像的维度，解码器则将低维潜变量扩展回原始图像分辨率。除了用随机权重初始化之外，这两个组件目前完全没有连接。我们需要一起训练它们，以便它们都能理解相同的潜变量表示。

为此将创建一个自动编码器模型，让输入数据依次通过编码器和解码器。然后训练它，使得解码图像与作为输入提供的原始图像之间的差异最小。如果成功，输出图像将与输入图像相似。这个过程很有用，因为它允许数据压缩，但当发现训练后可以分别使用这两个组件时，它就变得更加有趣了。训练是由的代码和第7章是一致的，唯一的区别就是需要一个GPU环境来训练，否则太慢了！因此在训练代码里添加了把数据送到GPU的代码，以及变量device。当device的值等于"cuda"时，表明系统使用GPU进行加速，否则device的值是"cpu"。

loss由原始的图像和经过重构的图像之间的差值而来。通常可以用MSE来计算。

    def mini_batch_train(data_loader,model,optimizer,loss_fn,device='cuda'):
        mini_batch_losses = []
        for x_batch, y_batch in data_loader:
            # 将数据放到GPU上
            x_batch = x_batch.to(device)
            y_batch = y_batch.to(device)
            # 置为训练状态
            model.train()
            # Step 1 - 前向计算预测值
            yhat = model(x_batch)
            # Step 2 - 计算损失
            mini_batch_loss = loss_fn(yhat, y_batch)
            # Step 3 - 计算梯度
            mini_batch_loss.backward()
            # Step 4 - 参数更新
            optimizer.step()
            optimizer.zero_grad()

            mini_batch_losses.append(mini_batch_loss.item())
                      
        loss = np.mean(mini_batch_losses)
        return loss

注意我们只有mini_batch_train，没有也不需要mini_batch_val。图片集里的所有图片都用于学习了。然后是train函数：

    def train(model, train_loader, test_loader, loss_fn, optimizer, epochs, device='cuda'):
        model.to(device)
        loss_fn.to(device)
        # 循环轮数计数
        total_epochs = 0

        losses = []  # 每轮训练的损失

        for epoch in range(epochs):
            model.train()
            total_epochs += 1

            # 进入mini-batch的内循环
            loss = mini_batch_train(train_loader,model,optimizer,loss_fn,device)
            losses.append(loss)
            print(f"Epoch {total_epochs}/{epochs}, Loss: {loss:.4f}")
        
        return losses

接下来是参数设置和训练：

    epochs = 100
    lr = 1e-3
    model = AutoEncoder(in_channels=3, out_channels=3)
    optimizer = optim.AdamW(model.parameters(), lr=lr, weight_decay=1e-5)
    loss_fn = nn.MSELoss()
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    train_losses = train(model, train_loader, None, loss_fn, optimizer, epochs, device=device)

训练部分的代码和第7章高度类似，就不再详细讲述了。训练后的loss图如下：

![](images8/media/image4.png){width="3.7595199037620297in"
height="1.4546380139982502in"}

图8-3 训练的损失图

**7. 单独使用解码器推理：**

    fake_image = torch.randn(5,256).to(device)
    with torch.inference_mode():
        reconstructed_image = model.decoder(fake_image)
    reconstructed_image.shape

我们随机产生了5个256维的向量，然后将它送入到解码器中得到5个重构的图像：

![狗的照片 AI
生成的内容可能不正确。](images8/media/image5.png){width="2.232252843394576in"
height="0.46607502187226596in"}

换言之，使用5个随机的向量产生了5幅新的图像！

### 8.4.3 变分自动编码器

在上一小节，实现了一个简单的自动编码器如何在低维潜在空间中学习输入数据的高效表示。自动编码器能够如实地对任何样本进行编码，并在之后对其进行恢复（或解码）。这对于特征提取或数据表示来说效果很好，但有时并不太适合生成新的样本。

原因在于自动编码器没有能力将表示分离到潜在空间中一致的部分。在潜在空间中，相似输入的表示通常聚集在彼此附近，但也存在大量的重叠和空白区域，分配给每个类别的潜在空间数量上也存在很大的差异。如果在潜在空间中选择一个随机点，并将其输入解码器，无法如实地预测会得到什么结果。

变分自动编码器（Variational
AutoEncoders，VAEs）通过学习潜在空间中每个特征的概率分布来解决这个问题。变分自动编码器不是将输入映射到特定的点，而是用高斯分布来表示每个特征，以此捕捉数据中该特征的可变性。

例如，一个由多种犬类和猫类图像组成的数据集。我们不知道编码器会提取出哪些特征，但可以想象，有些特征可能会用来表示诸如毛茸茸的斑块、眼睛、耳朵、腿或尾巴等特征。这些特征在数据集中的所有图像中可能会有很大程度的重叠（所有这些动物都有两只耳朵、四条腿和一条尾巴），但狗的耳朵和猫的耳朵在外观上也存在差异。"耳朵"这个特征可以用一个高斯分布来表示，这个分布涵盖了所有这些可变性，分布的均值代表了动物耳朵的平均形状。如果朝着不同的方向偏离均值，将会得到一个朝着各种可能出现在不同品种中的耳朵形状的连续且均匀的过渡。

使用这种方法，能够创建了一个更具结构化的潜在空间，从这些分布中进行采样使能够生成新的、合理的实例。与自动编码器一样，类别信息通常在变分自动编码器中也不被使用。现在看看如何对变分自动编码器进行编码和训练。

变分自动编码器（VAE）的编码器与上一节中的基本编码器非常相似。在上一节，使用了几个卷积层和一个全连接层（线性层）来投影到所需大小的潜在空间上。此处将使用相同的架构，唯一的区别在于不是使用一个线性层来预测图像的潜在空间，而是使用线性层来学习概率分布。一个概率分布由两个参数来表征，即均值和方差，所以需要两个线性层：

- 一个线性层学习分布的均值。

- 一个线性层学习分布的方差。

从代码的角度来看编码器是这样的：

    class VAEEncoder(nn.Module):
        def __init__(self, in_channels=3, latent_dim=256):
            super().__init__()
            self.con_block = nn.Sequential(
                # 3@64x64 -> 64@32x32
                nn.Conv2d(in_channels, 64, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(64),
                # 64@32x32 -> 128@16x16
                nn.Conv2d(64, 128, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(128),
                # 128@16x16 -> 256@8x8
                nn.Conv2d(128, 256, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(256),
                # 256@8x8 -> 512@4x4
                nn.Conv2d(256, 512, kernel_size=4, stride=2, padding=1),
                nn.ReLU(),
                nn.BatchNorm2d(512),
                # 512@4x4 -> 1024@1x1
                nn.Conv2d(512, 1024, kernel_size=4, stride=2, padding=0),
                nn.ReLU(),
                nn.BatchNorm2d(1024),
            )
            self.mu = nn.Linear(1024, latent_dim)
            self.logvar = nn.Linear(1024, latent_dim)
        
        def forward(self, x):
            x = self.con_block(x)
            # shape: (batch_size, 1024, 1, 1)
            x = x.flatten(start_dim=1)
            # shape: (batch_size, 1024)
            mu = self.mu(x)
            logvar = self.logvar(x)
            return mu, logvar      

如果将这段代码片段与上一节的编码器进行比较，会发现差异极小。此处有两个线性层而非一个，这两个层将分别从同一个卷积层输出中计算出两个不同的值，并在forward()方法中返回这两个值。这两个计算值的目的是表示概率分布的均值和方差。最初它们只是两个相同的线性层。挑战在于确保它们在训练过程中学会表示我们想要的东西------均值和方差。此处用mu表示均值，logvar表示方差的对数。使用方差的对数，而不是直接输出方差，主要是为了数值稳定性。

对于解码器无需做任何更改。变分自动编码器（VAE）与简单自动编码器之间的差异在于在潜在空间中找到一个点来表示输入项的方式，但解码器的任务是相同的：给定潜在空间中的一个点z，显示其编码表示与z最相似的图像。在自动编码器的情况下，z是卷积层提取的特征的线性投影。使用变分自动编码器（VAE）的编码器时，得到一个正态分布，然后从该分布中采样以获得z。因此，可以使用上一节的解码器，但需要修改模型以便从分布中采样。更新后的变分自编码器（VAE）编码器会返回一个正态分布的均值和方差，该正态分布试图与输入数据的表征相匹配。为了获得解码后的输出，必须从该分布中进行采样，如下代码片段所示：

    class VAE(nn.Module):
        def __init__(self, in_channels=3, latent_dim=256):
            super().__init__()
            self.encoder = VAEEncoder(in_channels=in_channels, latent_dim=latent_dim)
            self.decoder = Decoder(out_channels=in_channels)

        def reparameterize(self, mu, logvar):
            std = torch.exp(0.5 * logvar)
            # 从标准正态分布中采样，然后进行平移和缩放。
            eps = torch.randn_like(std)
            return mu + eps * std

        def forward(self, x):
            mu, logvar = self.encoder(x)
            z = self.reparameterize(mu, logvar)
            x_recon = self.decoder(z)
            return x_recon, mu, logvar

需要注意的是此处使用的是多维高斯分布，而不仅仅是实数的一维正态曲线。在这个变分自动编码器的示例中，对于均值和方差，都使用了潜在维度。可以使用任意数量的维度，就像自动编码器中使用的256维一样。一个实值（一维）正态分布表示为N(μ,σ^2^)，它由两个量来定义：μ，即分布的均值，以及*σ*，即标准差，它是方差σ^2^的平方根。正态分布的一个有用特性是，所有正态分布都可以根据标准正态分布来表示，标准正态分布的均值为0且方差为1，方法是通过对其进行平移和缩放：

$$N\left( \mu,\sigma^{2} \right) = \mu + \sigma N(0,1)$$

也就是说要从任意正态分布N(μ,σ^2^)中获取一个样本，可以改为从N(0,1)中采样，然后乘以σ并加上μ。

多维高斯分布被称为多元高斯分布。它们仍然可以由两个参数来定义，不同之处在于μ是一个向量，而σ（协方差矩阵，用Σ表示）是一个矩阵。因此，该分布被定义为N(μ,Σ)。如果该分布在所有维度上都是相互独立的，也就是说每个变量与其他变量都不相关且具有相同的方差，那么它就被称为各向同性分布。在各向同性的多元高斯分布中，协方差矩阵Σ是一个对角矩阵，其对角线上的所有元素都相等，可以表示为σI，其中I是单位矩阵。那么标准多元高斯分布就表示为N(0,
I)。

前面的变分自动编码器对一个多元、各向同性的高斯分布进行建模，因为没有理由认为样本坐标之间相互依赖（而且这样更简单）。这意味着可以使用所谓的重参数化技巧从标准高斯分布中采样，然后进行平移和缩放，以获得潜在空间向量。

关于稳定性，模型预测的是方差的对数，而不是方差，这样做是为了提高数值稳定性并便于训练。从数学角度来看，计算方差还是方差的对数并没有区别。但在实际应用中，我们知道方差始终是一个正数，并且通常接近0。然而，在开始训练时，模型并没有理由生成正值且较小的值。此外，数字是以浮点数格式表示的，这使得很难区分非常接近的数值。通过取对数，我们能得到两个好处：

- 将可接受的值的范围扩展到负无穷，这样模型就有更多的余地用浮点数来表示结果。

- 确保方差始终为正，因为方差是对数方差（logvar）的指数形式。

训练变分自动编码器的关键在于损失函数。在自动编码器中，使用的损失函数衡量的是重建图像与原始图像之间的差异。希望重建图像尽可能地与原始图像相似，但现在损失函数中引入了第二个因素，我们希望特征遵循高斯分布。实现这一目标的方法是利用分布之间的库尔贝克-莱布尼茨散度（也称为相对熵）。库尔贝克-莱布尼茨散度（KL
散度）是一种衡量一个概率分布与另一个概率分布差异程度的方法。对于各向同性的多元高斯分布而言，KL散度可以按如下方式计算。假设有两个各向同性的多元高斯分布P=N(μ~1~,σ~1~^2^I)和Q=N(μ~2~,σ~2~^2^I)，其中μ~1~和μ~2~是均值向量，σ~1~^2^和σ~1~^2^是方差，I是单位矩阵。则它们之间的KL散度*D~KL~*(*P*∣∣*Q*)为：

$$D_{KL}(P||Q) = - \frac{1}{2}\sum_{i = 1}^{n}{(\ln\frac{\sigma_{1i}^{2}}{\sigma_{2i}^{2}} - \frac{\sigma_{1i}^{2}}{\sigma_{2i}^{2}} - \frac{\left( \mu_{1i}^{2} + \mu_{2i}^{2} \right)}{\sigma_{2i}^{2}}} + 1)$$

在变分自编码器的训练中，通常希望将模型学习到的分布与标准正态分布N(0,
I)进行比较，即P是模型学习到的分布，Q是标准正态分布，那么KL散度的计算公式可以简化为：

$D_{KL} = - \frac{1}{2}\sum_{i = 1}^{n}{(ln(\sigma_{i}^{2}}) - \sigma_{i}^{2} - \mu_{i}^{2} + 1$)

其中n为正态分布的维度。为了计算损失，创建了一个名为VAELoss的类，在这里，损失由2部分构成：

- 解码器生成的图像与原始图像之间的均方误差（MSE）。这个损失因素与训练自动编码器时使用的损失因素相同。

- 根据刚刚给出的公式计算K~LD~项，将它们相加。

可以赋予其中一个或另一个更大的权重，以平衡重建保真度和与高斯分布的一致性。目前我们将它们直接相加，但尝试调整这种平衡是一个很好的实验。

    class VAELoss(nn.Module):
        def __init__(self):
            super().__init__()
            self.mse = nn.MSELoss(reduction='none')
        def forward(self, yhat, y):
            x_recon, mu, logvar = yhat
            mse_loss = self.mse(x_recon, y).sum(dim=(1,2,3))
            kl_loss = -0.5 * torch.sum(1 + logvar - mu.pow(2) - logvar.exp(), dim=-1)
            return (mse_loss + kl_loss).mean(dim=0)

到此。就可以使用和上一节一样的代码进行训练了。500epoches的损失图：

![图表 AI
生成的内容可能不正确。](images8/media/image6.png){width="5.201573709536308in"
height="2.012599518810149in"}

图8-4 VAE训练损失图

随机生成的5个头像：

![人的脸 AI
生成的内容可能不正确。](images8/media/image7.png){width="2.9046270778652667in"
height="0.6064610673665792in"}

### 8.4.5 diffusion模型生成图像

图像生成领域在伊恩·古德费洛于2014年引入生成对抗网络（GANs）后广泛流行起来。生成对抗网络的关键思想催生了一系列模型，这些模型能够快速生成高质量的图像。然而，尽管生成对抗网络取得了成功，但它也带来了一些挑战，比如需要大量参数，并且难以有效地进行泛化。这些局限性引发了一系列并行的研究工作，进而推动了对扩散模型的探索。扩散模型是一类能够重新定义高质量、灵活图像生成格局的模型。

2020年末，扩散模型开始在机器学习领域引起轰动。研究人员发现，使用这些扩散模型生成的图像质量比生成对抗网络生成的更高。随后出现了大量论文，提出了各种改进和修改方案，进一步提升了图像生成的质量。

到2021年末，像GLIDE这样的模型在文本转图像任务中展示出了令人惊叹的成果。仅仅几个月后，这些模型就随着DALL·E2和Stable
Diffusion等工具进入了主流应用领域。这些模型让任何人都能通过输入对想要看到的内容的文本描述轻松生成图像。

扩散模型的核心概念是，它们接收带有噪声的模糊图像，并学习对这些图像进行去噪处理，输出清晰的图像。在训练扩散模型时，数据集中包含具有不同噪声量的图像（即使输入的是纯噪声也不例外）。在推理过程中，可以从纯噪声开始，模型会生成符合训练分布的图像。该模型会进行多次迭代来实现这一目标，自我修正并生成高质量的图像（参看第6章，6.5.4节）。

那么，是什么让扩散模型如此强大呢？以前的技术，如变分自编码器（VAEs）或生成对抗网络（GANs），通过模型的单次前向传播生成最终输出。这意味着模型必须在第一次尝试时就把所有事情都做对。如果它犯了错误，就无法回头去修正。另一方面，扩散模型通过许多步骤的迭代来生成输出。这种迭代细化使模型能够纠正前一步中的错误，并逐步改进输出。为了说明这一点，可以使用Hugging
Face
diffusers库加载预训练的扩散模型。该库提供了一个高级管道，可用于直接创建图像。我们将加载ddpm-celebahq-256模型，这是最早共享的用于图像生成的扩散模型之一。该模型使用CelebA-HQ数据集进行训练，这是当时流行的高质量名人图像数据集，因此它生成的图像看起来就像是来自该数据集。我们将使用这个模型从噪声中生成一张图像（从Modelscope下载模型后8.1.2节，用模型实际路径取代from_pretrained的值）：

    import torch
    from diffusers import DDPMPipeline
    # 设置使用 GPU or CPU
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # 加载模型，改为实际存放模型的路径
    image_pipe = DDPMPipeline.from_pretrained("google/ddpm-celebahq-256")
    image_pipe.to(device)
    images = image_pipe().images
    images[0]

![黄色头发的女人 AI
生成的内容可能不正确。](images8/media/image8.png){width="1.6094575678040246in"
height="1.6094575678040246in"}

图8-5 生成的图像

如果运行这段代码，会注意到生成过程进行了1000步。这个扩散管道必须经过1000次细化步骤（和前向传播）才能得到最终的图像。与生成对抗网络（GANs）相比，这是普通扩散模型的主要缺点之一，它们需要很多步骤才能生成高质量的图像，这使得模型在推理时速度较慢。

可以逐步重新创建这个采样过程，以便更好地理解其内部发生的情况。在扩散过程开始时，用四张随机图像初始化样本x（换句话说，采样一些随机噪声）。我们将运行30步，逐步对输入图像去噪，最终得到来自真实分布的样本：

    # 随机起始点是4张图像 每张图像都是3通道（RGB）、256x256像素的图像
    image = torch.randn(4, 3, 256, 256).to(device)
    # 设置特定的扩散步骤数量
    image_pipe.scheduler.set_timesteps(num_inference_steps=30)
    for i, t in enumerate(image_pipe.scheduler.timesteps):
    # 根据当前样本x和时间步t获取预测结果
        with torch.inference_mode():
    # 我们需要传入时间步t，以便模型知道它当前处于哪个时间步。
            noise_pred = image_pipe.unet(image, t)["sample"]
    # 计算使用调度器后更新后的x
        scheduler_output = image_pipe.scheduler.step(noise_pred, t, image)
    # 更新x
        image = scheduler_output.prev_sample
    # 同时展示x和预测的去噪图像
        if i % 10 == 0 or i == len(image_pipe.scheduler.timesteps) - 1:
            plot_noise_and_denoise(scheduler_output, i)

plot_noise_and_denoise用于显示结果：

    from matplotlib import pyplot as plt
    from torchvision.utils import make_grid

    def plot_noise_and_denoise(scheduler_output, step):
        _, axs = plt.subplots(1, 2, figsize=(12, 5))

        prev_prev_sample = scheduler_output.prev_sample
        grid = make_grid(prev_prev_sample, nrow=4).permute(1, 2, 0)
        axs[0].imshow(grid.cpu().clip(-1, 1) * 0.5 + 0.5)
        axs[0].set_title(f"当前 x (step {step})")
        axs[0].axis("off")

        pred_x0 = scheduler_output.pred_original_sample
        grid = make_grid(pred_x0, nrow=4).permute(1, 2, 0)
        axs[1].imshow(grid.cpu().clip(-1, 1) * 0.5 + 0.5)
        axs[1].set_title(f"预测去噪后的图像 (step {step})")
        axs[1].axis("off")
        plt.show()

结果如图8-6。在图8-6图像的左侧，可以看到给定步骤的输入（从随机噪声开始）。在右侧看到模型对最终图像的预测。第一行的结果并不是特别好。在给定的扩散步骤中，不是直接跳到最终预测的图像，而是仅朝着预测的方向对输入x（显示在左侧）进行少量修改。然后将这个新的、稍好一些的x再次输入模型进行下一步，希望能得到稍好一些的预测，从而可以进一步更新x，依此类推。经过足够多的步骤，模型可以生成一些逼真的图像。

对上面的代码做一些简单的解释：

在使用DDPMPipeline 进行扩散模型推理时，scheduler（调度器）的
timesteps控制着去噪过程的步数。scheduler.set_timesteps(num_inference_steps)这是一个方法，用于自定义推理时的时间步数。在推理阶段，可以通过减少时间步数来加速生成过程，但可能会降低图像质量。num_inference_steps是希望使用的去噪步数（整数），必须小于等于模型预训练时的步数（例如，预训练时用了1000
步，推理时可以设为30 步以加速）。

![图形用户界面 AI
生成的内容可能不正确。](images8/media/image9.png){width="6.0in"
height="4.586805555555555in"}

图8-6 图像的去噪生成过程

在扩散模型的采样循环中，i（迭代索引）和t（时间步值）是两个关键变量，t表示当前去噪步骤的噪声水平，是调度器中timesteps列表的实际元素。取值范围通常从较大值（如1000）递减到较小值（如1），对应噪声从高到低的过程。模型根据t计算当前噪声的衰减率，并预测噪声的逆过程（即从噪声图像恢复为清晰图像）。i表示当前循环的迭代次数（从0开始），用于追踪整个去噪过程的进度。

noise_pred = image_pipe.unet(image,
t)\[\"sample\"\]这个语句中，函数参数imag表示当前时间步的带噪图像（形状通常为\[batch_size,
channels, height,
width\]）。t是当前时间步值（表示噪声水平）。noise_pred表示模型对当前输入图像中噪声的估计形状与image相同。

函数unet的输出是一个**字典**，包含多个预测结果。\"sample\" 是字典中的一个键，表示模型的**主要预测值**（即噪声）。

scheduler_output = image_pipe.scheduler.step(noise_pred, t, image)\`
是扩散模型推理过程中的核心步骤，负责根据预测噪声更新图像。扩散模型的核心是去噪过程，从纯噪声开始，逐步移除噪声，最终生成清晰图像。这一步骤由调度器（Scheduler）控制，它根据当前时间步的噪声预测noise_pred，计算如何更新当前图像（image）。具体来说，scheduler.step()完成以下操作：

- 根据当前噪声水平t和预测噪声noise_pred，计算下一个时间步的图像。

- 应用特定的采样算法（如DDPM、DDIM、PNDM等），平衡去噪速度和质量。

函数返回值scheduler_output是一个包含多个字段的对象（具体类型取决于调度器），通常包含：

- prev_sample：一个时间步的图像（即去噪后的新图像）。这是最核心的返回值，用于后续迭代。

- pred_original_sample：模型对原始图像（即完全不含噪声的图像）的预测。这在某些调度器中可用，用于可视化中间结果。

- 其他字段：某些调度器可能返回额外信息，如预测的噪声方差（variance_pred）或时间步（prev_timestep）。

### \*8.4.6 生成音频

机器学习在音频上最常见的两项任务是将语音转录为文本（自动语音识别，简称ASR），以及从文本生成语音（文本转语音）。在自动语音识别中，模型接收某人（或多人）讲话的音频作为输入，并输出相应的文本。对于某些模型，输出还会捕捉额外信息，比如说话的人是谁，或者某人在什么时间说了什么。自动语音识别系统应用广泛，从虚拟语音助手到字幕生成器都有使用。在文本转语音（TTS）中，模型生成合成的、且希望能逼真的语音。文本转语音也面临着自身的一系列挑战，比如生成多个说话者的音频，让声音听起来更自然，以及在生成过程中融入语调、停顿、情感标记、音高控制、口音和其他特征。

虽然语音合成（TTS）和自动语音识别（ASR）是最受欢迎的任务，但还可以利用机器学习和音频做许多其他事情：

- 文本转音频：文本转语音可以扩展为文本转音频（TTA），即基于一个提示，模型可以生成旋律、音效和歌曲。

- 语音克隆：保留一个人的声音，包括语调、音高和韵律，以生成新的声音。

- 音频分类：模型对提供的音频进行分类。典型的例子有命令识别和说话人识别。

- 语音增强：模型从音频中去除噪声，使语音更清晰。

- 音频翻译：模型接收源语言X的音频，并输出目标语言Y的音频。

- 说话人分离：模型识别特定时间的说话人。

由于多种原因，音频相关任务颇具挑战性。首先，处理原始音频信号比处理文本更为复杂，也不那么直观。对于许多应用而言，音频模型需要实时运行或在设备上运行，这会限制模型的大小和推理速度。例如，如果想将当前的扩散模型用于交互式翻译，其速度会太慢。最后，评估生成式音频模型也颇具难度。如何衡量模型生成的歌曲质量是否良好呢？

在语音处理与生成领域，如今能够借助丰富多样的工具，以及海量开放获取的模型和数据集，高效完成各类复杂任务。在数据集方面，由Mozilla基金会推出的"通用语音库"（Common
Voice）堪称众包数据集的典范，它汇聚了全球志愿者贡献的超过2000小时音频文件及对应文本，覆盖一百多种语言，为多语言语音研究提供了坚实基础。与此同时，LibriSpeech、VoxPopuli和GigaSpeech等广受欢迎的音频数据集也备受研究者青睐，它们各自聚焦不同领域，适用于多样化的应用场景。

在模型层面，有基于英文的Meta的Wav2Vec2、OpenAI的Whisper、微软的SpeechT5，也有颇具创新力的Suno公司开发的Bark模型。此外，扩散模型在音频生成领域的应用也令人瞩目，例如将Stable
Diffusion技术迁移至歌曲生成，还有Dance
Diffusion和AudioLDM等，这些模型为音频创作带来了全新思路和无限可能。虽然从传统语音处理跨越到音频生成领域看似充满挑战，但此前在生成式领域探索中积累的工具与经验，将成为攻克难题的有力武器，助力我们在语音与音频的创新之路上不断前行。

英文和中文毕竟还是有很大的差别的，国内应用广泛的开源中文语音模型及其特点，简要叙述如下：

**语音识别（ASR）模型**

- DeepSpeech：开发者为百度，基于端到端架构，支持多语言（含中文），提供预训练模型和训练框架。主要应用于实时语音转写、语音助手。

- Wenet：开发者为阿里巴巴达摩院，支持流式和非流式识别，提供中文预训练模型，适配低资源场景。主要应用于智能客服、会议纪要生成。

- Paraformer：开发者为字节跳动，基于Transformer架构，在中文普通话识别上精度领先，支持标点预测。主要应用于长文本语音识别、视频字幕生成。

**语音合成（TTS）模型**

- Bark：开发者为Suno（国际团队，但社区有中文优化版本）。支持文本到语音和歌声合成，可生成富有情感的中文语音。主要应用场景于有声书制作、短视频配音。

- VITS：开发者Meta（国际），但国内有大量中文微调版本。端到端语音合成，支持多说话人，中文音色自然度高。主要应用场景于语音助手、广播剧配音。

- Chinese-VITS2：开发者为国内社区。基于VITS2架构，专注中文语音合成，支持自定义音色训练。主要应用场景于游戏语音、虚拟主播。

这些模型均在GitHub或Hugging
Face上开源，附带详细文档和示例，适合个人开发者和企业快速集成。如需特定领域优化（如方言识别），可基于预训练模型进行微调。

