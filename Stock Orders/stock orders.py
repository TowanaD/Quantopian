def initialize(context):
    context.plug = sid(20776)
    
def handle_data(context, data):
    hist = data.history(context.plug,'price', 50, '1d')
    log.info(hist.head())
    sma_50 = hist.mean()
    sma_20 = hist[-20:].mean()
    
    if sma_20 > sma_50:
        order_target_percent(context.plug, 1.0)
    elif sma_50 > sma_20:
        order_target_percent(context.plug, -1.0)