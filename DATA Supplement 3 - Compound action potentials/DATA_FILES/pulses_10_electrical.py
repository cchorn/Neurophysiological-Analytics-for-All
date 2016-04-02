"""
this code produces 10 CAPS that extend from infinity to 0.3 m/s
"""

# print stim times and convert to a numpy array
print(stims)
stims1 = np.array(stims['Time'])

#Select timestamp for each pulse
s1 = stims1[0]; s2 = stims1[1]; s3 = stims1[2]; s4 = stims1[3]; s5 = stims1[4]; s6 = stims1[5]; s7 = stims1[6]; s8 = stims1[7]; s9 = stims1[8]; s10 = stims1[9]

#select 10 CAPs (compound action potentials)
start1 = np.rint((s1 * 20000)); end1 = np.rint((start1 + 3000)); start2 = np.rint((s2 * 20000)); end2 = np.rint((start2 + 3000)); start3 = np.rint((s3 * 20000)); end3 = np.rint((start3 + 3000)); start4 = np.rint((s4 * 20000)); end4 = np.rint((start4 + 3000)); start5 = np.rint((s5 * 20000)); end5 = np.rint((start5 + 3000)); start6 = np.rint((s6 * 20000)); end6 = np.rint((start6 + 3000)); start7 = np.rint((s7 * 20000)); end7 = np.rint((start7 + 3000)); start8 = np.rint((s8 * 20000)); end8 = np.rint((start8 + 3000)); start9 = np.rint((s9 * 20000)); end9 = np.rint((start9 + 3000)); start10 = np.rint((s10 * 20000)); end10 = np.rint((start10 + 3000))
T1 = asig[start1:end1]; T2 = asig[start2:end2]; T3 = asig[start3:end3]; T4 = asig[start4:end4]; T5 = asig[start5:end5]; T6 = asig[start6:end6]; T7 = asig[start7:end7]; T8 = asig[start8:end8]; T9 = asig[start9:end9]; T10 = asig[start10:end10]

# plot each individual CAP
plotname1 = name + '-individual.svg'
time = np.arange(0,150,0.05) # make a time variable
fig, (ax1,ax2,ax3,ax4,ax5,ax6,ax7,ax8,ax9,ax10) = plt.subplots(nrows=10,sharex=True,sharey=True,figsize = (8, 8))
ax1.plot(time,T1)
ax1.set_title('10 Compound action potentials (CAPs)', fontsize=20)
ax1.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax2.plot(time,T2)
ax2.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax3.plot(time,T3)
ax3.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax4.plot(time,T4)
ax4.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax5.plot(time,T5)
ax5.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax6.plot(time,T6)
ax6.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax7.plot(time,T7)
ax7.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax8.plot(time,T8)
ax8.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax9.plot(time,T9)
ax9.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax10.plot(time,T10)
ax10.tick_params(axis='both',which='both',bottom='on',top='off',right='off')
ax10.set_xlabel('Time [ms]', fontsize=18)
fig.text(0.04, 0.5, 'microvolts', ha='center',fontsize=18,rotation='vertical')
ax10.set_yticks(range(-100,110,100))
plt.savefig('OUTPUT_FILES/' + plotname1)
plt.show()

# compute the average CAP
ave1 = np.mean([T1,T2,T3,T4,T5,T6,T7,T8,T9,T10], axis = 0)

# plot the average CAPs
plotname2 = name + '-average.svg'
time = np.arange(0,150,0.05) # make a time variable
fig, (ax1) = plt.subplots(nrows=1,sharex=True,sharey=True,figsize = (8, 8))
ax1.set_title('Average CAP', fontsize=20)
ax1.plot(time,ave1)
ax1.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax1.set_yticks(np.arange(-100,120,100))
ax1.set_xlabel('Time [ms]', fontsize=18)
fig.text(0.04, 0.5, 'microvolts', ha='center',fontsize=18,rotation='vertical')
plt.savefig('OUTPUT_FILES/' + plotname2)
plt.show()

# compute rectification
ave_rect1 = np.absolute(ave1)

# plot the rectified CAPs
plotname3 = name + '-rectified.svg'
time = np.arange(0,150,0.05) # make a time variable
fig, (ax1) = plt.subplots(nrows=1,sharex=True,sharey=True,figsize = (8, 8))
ax1.set_title('Averaged and Rectified CAP', fontsize=20)
ax1.plot(time,ave_rect1)
ax1.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax1.set_xlabel('Time [ms]', fontsize=18)
fig.text(0.04, 0.5, 'microvolts', ha='center',fontsize=18,rotation='vertical')
plt.savefig('OUTPUT_FILES/' + plotname3)
plt.show()
# export data into a CSV file
FINAL1 = pd.DataFrame({'rect':ave_rect1})
name1 = name + '_analog.csv'
FINAL1.to_csv('OUTPUT_FILES/' + name1)

# determine latency in ms for each velocity starting with 0.25 m/s or 0.25 mm/ms
# e.g., 0.3 = 40 mm / 133.3 ms ... which is 133.3 ms = 40 / 0.3
ms40 = vag_length / 0.3 #0.30 m/s
ms39 = ms40 * (1-1/39) #0.31 m/s
ms38 = ms40 * (1-1/38) #0.32 m/s
ms37 = ms40 * (1-1/37) #0.32 m/s
ms36 = ms40 * (1-1/36) #0.33 m/s
ms35 = ms40 * (1-1/35) #0.34 m/s
ms34 = ms40 * (1-1/34) #0.35 m/s
ms33 = ms40 * (1-1/33) #0.36 m/s
ms32 = ms40 * (1-1/32) #0.38 m/s
ms31 = ms40 * (1-1/31) #0.39 m/s
ms30 = ms40 * (1-1/30) #0.40 m/s
ms29 = ms40 * (1-1/29) #0.41 m/s
ms28 = ms40 * (1-1/28) #0.43 m/s
ms27 = ms40 * (1-1/27) #0.44 m/s
ms26 = ms40 * (1-1/26) #0.46 m/s
ms25 = ms40 * (1-1/25) #0.48 m/s
ms24 = ms40 * (1-1/24) #0.50 m/s
ms23 = ms40 * (1-1/23) #0.52 m/s
ms22 = ms40 * (1-1/22) #0.55 m/s
ms21 = ms40 * (1-1/21) #0.57 m/s
ms20 = ms40 * (1-1/20) #0.60 m/s
ms19 = ms40 * (1-1/19) #0.63 m/s
ms18 = ms40 * (1-1/18) #0.67 m/s
ms17 = ms40 * (1-1/17) #0.71 m/s
ms16 = ms40 * (1-1/16) #0.75 m/s
ms15 = ms40 * (1-1/15) #0.80 m/s
ms14 = ms40 * (1-1/14) #0.86 m/s
ms13 = ms40 * (1-1/13) #0.92 m/s
ms12 = ms40 * (1-1/12) #1.00 m/s
ms11 = ms40 * (1-1/11) #1.09 m/s
ms10 = ms40 * (1-1/10) #1.20 m/s
ms9 = ms40 * (1-1/9) #1.33 m/s
ms8 = ms40 * (1-1/8) #1.50 m/s
ms7 = ms40 * (1-1/7) #1.71 m/s
ms6 = ms40 * (1-1/6) #2.00 m/s
ms5 = ms40 * (1-1/5) #2.40 m/s
ms4 = ms40 * (1-1/4) #3.00 m/s
ms3 = ms40 * (1-1/3) #4.00 m/s
ms2 = ms40 * (1-1/2) #6.00 m/s
ms1 = ms40 * (1-1/1) #12.00 m/s

# make an array for the latencies
Lat = np.around([ms1,ms2,ms3,ms4,ms5,ms6,ms7,ms8,ms9,ms10,ms11,ms12,ms13,ms14,
        ms15,ms16,ms17,ms18,ms19,ms20,ms21,ms22,ms23,ms24,ms25,ms26,ms27,ms28,
        ms29,ms30,ms31,ms32,ms33,ms34,ms35,ms36,ms37,ms38,ms39,ms40], decimals=2)
# make an array for the velocities
Con = np.around([vag_length / x for x in Lat], decimals=2)
# divide averaged rectified array into 40 parts
size = int((ms40 / 40) * 40) #multiply by 40 because there are 20 pts in every ms ... and convert to an integer because it gives a warning

# set up some parameters for the plot
bins = 40
index = np.arange(bins)
bar_width = 1
opacity = 0.4
ticks = ('12.00','6.00','4.00','3.00','2.40','2.00','1.71','1.50','1.33','1.20',
        '1.09','1.00','0.92','0.86','0.80','0.75','0.71','0.67','0.63','0.60','0.57',
        '0.55','0.52','0.50','0.48','0.46','0.44','0.43','0.41','0.40','0.39','0.38',
        '0.36','0.35','0.34','0.33','0.32','0.32','0.31','0.30')

# select the 40 parts from each averaged and rectified signal
# essentially this is just a conversion of a numpy array from 1D to 2D
ave_rect1bin = np.reshape(ave_rect1,(bins,75))

#Compute the areas for each of the 20 parts using the composite trapezoidal rule. http://docs.scipy.org/doc/numpy/reference/generated/numpy.trapz.html
areas1 = np.trapz(ave_rect1bin, dx=1)

# plot the areas
plotname4 = name + '-area.svg'
fig, (ax1) = plt.subplots(nrows=1,sharex=True,sharey=True,figsize = (8, 8))
ax1.bar(index, areas1, bar_width, alpha=opacity, color='black')
ax1.tick_params(axis='both',which='both',bottom='off',top='off',right='off')
ax1.set_xticks(range(1,40))
ax1.set_xticklabels(ticks, rotation='vertical')
fig.text(0.5, 0.04, 'Conduction Velocity (m/s)', ha='center',fontsize=18)
fig.text(0.04, 0.5, 'AUC', ha='center',fontsize=18,rotation='vertical')
ax1.set_title('Area under the curve (AUC)', fontsize=20)
plt.savefig('OUTPUT_FILES/' + plotname4)
plt.show()
# export data into a CSV file
FINAL2 = pd.DataFrame({'area': areas1})
name2 = name + '_AUC.csv'
FINAL2.to_csv('OUTPUT_FILES/' + name2)
