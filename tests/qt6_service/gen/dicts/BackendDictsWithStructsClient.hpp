/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/05.2_dictionaries_with_structs.yml
 *   Object: DictsWithStructs
 *   Template: qt6/client_header.j2
 */
#pragma once
#include <QObject>
#include <qqmlintegration.h>
#include <QDBusMessage>
#include <QDBusServiceWatcher>
#include <QDBusPendingCallWatcher>
#include <QVariant>
#include "DBusError.hpp"
#include "StructDict.hpp"
#include "SimonsDict.hpp"
#include "types.hpp"
namespace gen::dicts {

namespace BackendDictsWithStructsClientUtils {

/**
 * @brief Pending call object for the DictsStructMethod method calls.
 */
class DictsStructMethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    DictsStructMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an DictsStructMethod call returns.
     *
     * @param more numbers
     */
    void finished(const QMap<QString, SimonsDict> &reply);

    /**
     * @brief Emitted when an error ocurred during an DictsStructMethod call.
     *
     * @param error the error
     */
    void error(DBusError error);
private slots:
    void callFinished(QDBusPendingCallWatcher *watcher);
private:
    QDBusPendingCallWatcher m_watcher;
};

}

/**
 * D-Bus client for the com.yarpc.backend.dictsWithStructs D-Bus interface
 */
class BackendDictsWithStructsClient : public QObject {
    Q_OBJECT
    QML_ELEMENT
    /**
     * @brief Whether the client is connected.
     */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged)
    /**
     * @brief a simple property
     */
    Q_PROPERTY(QVariant dictStructProperty READ getVariantDictStructProperty WRITE setVariantDictStructProperty NOTIFY dictStructPropertyChanged)

public:
    BackendDictsWithStructsClient(QObject* parent = nullptr);

    /**
     * @brief a simple method with one argument
     *
     * @param numbers Some numbers
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendDictsWithStructsClientUtils::DictsStructMethodPendingCall* DictsStructMethod(
        QMap<QString, StructDict> numbers
    );

    /**
     * @brief Getter for the DictStructProperty property.
     *
     * @returns the current value of the property
     *
     * a simple property
     */
    QMap<QString, StructDict> getDictStructProperty() const;

    /**
     * @brief Setter for the DictStructProperty property.
     *
     * @param newValue the new value of the property
     *
     * a simple property
     */
    void setDictStructProperty(const QMap<QString, StructDict> &newValue);

public slots:
    /**
     * @brief Returns whether the target service is available.
     *
     * @returns Whether the target service is available.
     */
    bool getConnected() const;

    /**
     * @brief Returns a map containing the current values of all properties.
     *
     * @returns a map containing the current values of all properties
     */
    QVariantMap getAllProperties() const;

    /**
     * @brief a simple method with one argument
     *
     * @param numbers Some numbers
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendDictsWithStructsClientUtils::DictsStructMethodPendingCall* DictsStructMethod(
        QVariant numbers
    );

signals:
    /**
     * @brief Emitted when the connected property changes.
     */
    void connectedChanged();

    /**
     * @brief a simple signal with one argument
     *
     * @param numbers numbers
     */
    void dictStructSignalReceived(
        QVariant numbers
    );

    /**
     * @brief Changed signal for the DictStructProperty property.
     *
     * a simple property
     */
    void dictStructPropertyChanged();

private slots:
    void connectedHandler(const QString& service);
    void disconnectedHandler(const QString& service);
    void propertiesChangedHandler(QString interface, QVariantMap changes, QStringList);
    void DictStructSignalDBusHandler(QDBusMessage content);

    /**
     * @brief Getter for the DictStructProperty property as variant.
     *
     * @returns the current value of the property as variant
     *
     * a simple property
     */
    QVariant getVariantDictStructProperty() const;

    /**
     * @brief Setter for the DictStructProperty property as variant.
     *
     * @param newValue the new value of the property wrapped in a variant
     *
     * a simple property
     */
    void setVariantDictStructProperty(QVariant newValue);
private:
    bool m_connected = false;
    QDBusServiceWatcher m_watcher;
};

}