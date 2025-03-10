/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/06.1_enums.yml
 *   Object: Enums
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
#include "EnumStruct.hpp"
#include "Color.hpp"
#include "types.hpp"
namespace gen::enums {

namespace BackendEnumsClientUtils {

/**
 * @brief Pending call object for the EnumMethod method calls.
 */
class EnumMethodPendingCall : public QObject {
    Q_OBJECT
    QML_UNCREATABLE("")
    QML_ELEMENT
public:
    EnumMethodPendingCall(QDBusPendingCall pendingCall, QObject *parent);
signals:
    /**
     * @brief Emitted when an EnumMethod call returns.
     *
     * @param another color
     */
    void finished(const Color::Type &reply);

    /**
     * @brief Emitted when an error ocurred during an EnumMethod call.
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
 * D-Bus client for the com.yarpc.backend.enums D-Bus interface
 */
class BackendEnumsClient : public QObject {
    Q_OBJECT
    QML_ELEMENT
    /**
     * @brief Whether the client is connected.
     */
    Q_PROPERTY(bool connected READ getConnected NOTIFY connectedChanged)
    /**
     * @brief a property
     */
    Q_PROPERTY(QVariant enumProperty READ getVariantEnumProperty WRITE setVariantEnumProperty NOTIFY enumPropertyChanged)

public:
    BackendEnumsClient(QObject* parent = nullptr);

    /**
     * @brief a simple method with one argument
     *
     * @param color a color
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendEnumsClientUtils::EnumMethodPendingCall* EnumMethod(
        Color::Type color
    );

    /**
     * @brief Getter for the EnumProperty property.
     *
     * @returns the current value of the property
     *
     * a property
     */
    Color::Type getEnumProperty() const;

    /**
     * @brief Setter for the EnumProperty property.
     *
     * @param newValue the new value of the property
     *
     * a property
     */
    void setEnumProperty(const Color::Type &newValue);

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
     * @param color a color
     *
     * @returns Pending call object with finished signal containing the reply.
     */
    BackendEnumsClientUtils::EnumMethodPendingCall* EnumMethod(
        QVariant color
    );

signals:
    /**
     * @brief Emitted when the connected property changes.
     */
    void connectedChanged();

    /**
     * @brief a simple signal with one argument
     *
     * @param color a color
     */
    void enumSignalReceived(
        QVariant color
    );

    /**
     * @brief Changed signal for the EnumProperty property.
     *
     * a property
     */
    void enumPropertyChanged();

private slots:
    void connectedHandler(const QString& service);
    void disconnectedHandler(const QString& service);
    void propertiesChangedHandler(QString interface, QVariantMap changes, QStringList);
    void EnumSignalDBusHandler(QDBusMessage content);

    /**
     * @brief Getter for the EnumProperty property as variant.
     *
     * @returns the current value of the property as variant
     *
     * a property
     */
    QVariant getVariantEnumProperty() const;

    /**
     * @brief Setter for the EnumProperty property as variant.
     *
     * @param newValue the new value of the property wrapped in a variant
     *
     * a property
     */
    void setVariantEnumProperty(QVariant newValue);
private:
    bool m_connected = false;
    QDBusServiceWatcher m_watcher;
};

}