from multiprocessing import shared_memory

if __name__ == "__main__":
    currentOffers = shared_memory.ShareableList([])

    
