from pySpeechFeatures import mfcc
# from pySpeechFeatures import delta
# from pySpeechFeatures import logfbank
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np

(rate, sig) = wav.read("data/english.wav")
mfcc_feat = mfcc(sig, rate)
# d_mfcc_feat = delta(mfcc_feat, 2)
# fbank_feat = logfbank(sig, rate)

# print(fbank_feat[1:3, :])

F = np.transpose(mfcc_feat)

# print len(F)
fig, ax = plt.subplots(figsize=(12, 15))
fig.suptitle('pySpeechFeatures', fontsize=14, fontweight='bold')

plt.subplot(13, 1, 1); plt.plot(F[0, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #1');
plt.subplot(13, 1, 2); plt.plot(F[1, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #2');
plt.subplot(13, 1, 3); plt.plot(F[2, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #3');
plt.subplot(13, 1, 4); plt.plot(F[3, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #4');
plt.subplot(13, 1, 5); plt.plot(F[4, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #5');
plt.subplot(13, 1, 6); plt.plot(F[5, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #6');
plt.subplot(13, 1, 7); plt.plot(F[6, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #7');
plt.subplot(13, 1, 8); plt.plot(F[7, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #8');
plt.subplot(13, 1, 9); plt.plot(F[8, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #9');
plt.subplot(13, 1, 10); plt.plot(F[9, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #10');
plt.subplot(13, 1, 11); plt.plot(F[10, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #11');
plt.subplot(13, 1, 12); plt.plot(F[11, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #12');
plt.subplot(13, 1, 13); plt.plot(F[12, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #13');

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
