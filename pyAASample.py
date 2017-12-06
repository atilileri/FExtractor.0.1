# from pyAudioAnalysis import audioTrainTest as aT
# aT.featureAndTrain(["data/uniform_ah_18/1", "data/uniform_ah_18/2"], 1.0, 1.0,
#                    aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)
# aT.fileClassification("data/doremi.wav", "svmSMtemp", "svm")


from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import audioFeatureExtraction
import matplotlib.pyplot as plt
[Fs, x] = audioBasicIO.readAudioFile("data/english.wav");
F = audioFeatureExtraction.stFeatureExtraction(x, Fs, 0.050*Fs, 0.025*Fs);
# print len(F)

'''
Feature ID	Feature Name	    Description
1	        Zero Crossing Rate	The rate of sign-changes of the signal during the duration of a particular frame.
2	        Energy	            The sum of squares of the signal values, normalized by the respective frame length.
3	        Entropy of Energy	The entropy of sub-frames' normalized energies. It can be interpreted as a measure of abrupt changes.
4	        Spectral Centroid	The center of gravity of the spectrum.
5	        Spectral Spread	    The second central moment of the spectrum.
6	        Spectral Entropy	Entropy of the normalized spectral energies for a set of sub-frames.
7	        Spectral Flux	    The squared difference between the normalized magnitudes of the spectra of the two successive frames.
8	        Spectral Rolloff	The frequency below which 90% of the magnitude distribution of the spectrum is concentrated.
9-21	    MFCCs	            Mel Frequency Cepstral Coefficients form a cepstral representation where the frequency bands are not linear but distributed according to the mel-scale.
22-33	    Chroma Vector	    A 12-element representation of the spectral energy where the bins represent the 12 equal-tempered pitch classes of western-type music (semitone spacing).
34	        Chroma Deviation	The standard deviation of the 12 chroma coefficients.
'''
fig, ax = plt.subplots(figsize=(12, 15))
fig.suptitle('pyAudioAnalysis', fontsize=14, fontweight='bold')

plt.subplot(13, 1, 1); plt.plot(F[8, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #1');
plt.subplot(13, 1, 2); plt.plot(F[9, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #2');
plt.subplot(13, 1, 3); plt.plot(F[10, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #3');
plt.subplot(13, 1, 4); plt.plot(F[11, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #4');
plt.subplot(13, 1, 5); plt.plot(F[12, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #5');
plt.subplot(13, 1, 6); plt.plot(F[13, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #6');
plt.subplot(13, 1, 7); plt.plot(F[14, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #7');
plt.subplot(13, 1, 8); plt.plot(F[15, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #8');
plt.subplot(13, 1, 9); plt.plot(F[16, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #9');
plt.subplot(13, 1, 10); plt.plot(F[17, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #10');
plt.subplot(13, 1, 11); plt.plot(F[18, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #11');
plt.subplot(13, 1, 12); plt.plot(F[19, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #12');
plt.subplot(13, 1, 13); plt.plot(F[20, :]); plt.xlabel('Frame no'); plt.ylabel('MFCC #13');

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

