import math


def spatial_pyramid_pool(self,previous_conv, num_sample, previous_conv_size, out_pool_size):
    """
    Args:
        previous_conv: a tensor vector of previous convolution layer
        num_sample: an int number of image in the batch
        previous_conv_size: an int vector [height, width] of the matrix features size of previous convolution layer
        out_pool_size: a int vector of expected output size of max pooling layer
    Returns:
        a tensor vector with shape [1 x n] is the concentration of multi-level pooling
    """
    # print('previous_conv.size()', previous_conv.size())
    
    global spp
    for i in range(len(out_pool_size)):
        # print(previous_conv_size)
        # size of window
        h_wid = int(math.ceil(previous_conv_size[0] / out_pool_size[i]))
        w_wid = int(math.ceil(previous_conv_size[1] / out_pool_size[i]))
        
        # stride
        h_str = int(math.floor(previous_conv_size[0] / out_pool_size[i]))
        w_str = int(math.floor(previous_conv_size[1] / out_pool_size[i]))
        
        maxpool = nn.MaxPool2d((h_wid, w_wid), stride=(h_str, w_str))
        x = maxpool(previous_conv)
        if i == 0:
            spp = x.view(num_sample,-1)
            # print("spp size:",spp.size())
        else:
            # print("size:",spp.size())
            spp = torch.cat((spp,x.view(num_sample,-1)), 1)
    return spp
